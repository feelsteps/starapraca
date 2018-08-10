#C:/Users/filip.stepniak/Projects/1_Project_Leviathan/test_dataset/out/freelancermap/projects/rfc_project_30-07-2018.json
import numpy as np
import pandas as pd
import json
from fuzzywuzzy import process, fuzz
import time
import pdb
import math
from datetime import datetime
import sys
import os

today_date = datetime.today().strftime("%d_%m_%Y_%H_%M_%S")

#userinput of the path
userInput = input("Enter the path of your file: ")
assert os.path.exists(userInput), "I did not find the file "+str(userInput)

# load geoData and prepare
geoRead = pd.read_csv('C:/Users/filip.stepniak/Projects/1_Project_Leviathan/GeoLiteCity_20180327/GeoLiteCity-Location.csv',
                    encoding = "ISO-8859-1",low_memory=False, header=1)
geoSelected = geoRead[geoRead['country']=='DE'][['city','latitude','longitude']].dropna()
geoGrouped = geoSelected.groupby('city').median().reset_index()

#load scrapyData 
with open(userInput) as json_file:
    d = json.load(json_file)
dfRead=pd.DataFrame(d) 

#data cleansing projects 
toBeRemoved = ["remote","Remote","DE",")","(","Großraum","Umgebung","GR","Raum","Region","Deutschland","Stadtgebiet","Norddeutschland","\d+"]
for i in toBeRemoved:
    dfRead['location']=dfRead['location'].str.replace(i,'')
dfRead['location']=dfRead['location'].str.replace('Munich','München')
dfRead['location']=dfRead['location'].str.replace('NRW','Nordrhein-westfalen')
dfRead['location']=dfRead['location'].str.replace('berlin','Berlin')

dfTransform = dfRead.groupby('location').count().reset_index()[['location','duration']].rename(index=str,columns={'location': 'city', 'duration': 'suma'})

#text mining function with threshold 
choicesForFuzzy = geoGrouped['city']
def compare_cities(query):
    high_ratio_cities = []
    maxratecity = 0
    for city in choicesForFuzzy:
        if fuzz.ratio(query,city) >= 65:
            high_ratio_cities.append((city,fuzz.ratio(query,city)))         
    maxratecity = max(high_ratio_cities,key=lambda x:x[1]) if len(high_ratio_cities) > 0 else maxratecity
    if maxratecity != 0:
        return maxratecity[0]
    else:
        return 0
    
#fuzzy wuzzy - it takes longer 
fuzzy = []
for city in dfTransform['city']:
    fuzzy.append(compare_cities(city))
    
#replace city with newcity
newCity = pd.Series(fuzzy)
dfTransform['newCity'] = newCity.values
print ('\nthe number of unmatched:',sum(dfTransform[dfTransform['newCity']==0]['suma']))

#groupby newcity
dfGrouped = dfTransform.groupby('newCity').sum().reset_index().rename(columns={'newCity':'city'})

#merge with the GeoData + drop missing values 
dfMerged = pd.merge(dfGrouped,geoGrouped,how='left', left_on='city',right_on='city').dropna()

#export to csv
dfMerged.to_csv('fmMapProjects_'+today_date+'.csv')
print ('\ndata successfully saved')