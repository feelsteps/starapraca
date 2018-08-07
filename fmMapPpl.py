#C:/Users/filip.stepniak/Projects/1_Project_Leviathan/test_dataset/out/freelancermap/people/rfc_people_30-07-2018.json
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
geoGrouped=geoSelected.groupby('city').median().reset_index()

#load scrappyData 
with open(userInput) as json_file:
    d = json.load(json_file)
#DataFrame from json file 
dfRead=pd.DataFrame(d) 
len(dfRead)

#getting a list of cities out of column location for fuzzy wuzzy
cities_list = []
for stadt in dfRead['location']:
    cities_list.append(stadt.split("|")[1])
dfRead['city'] = cities_list
dfRead['suma'] = 1
dfTransform = dfRead.groupby('city').count().reset_index()[['city','suma']]

#similarities with fuzzy wuzzy
choicesForFuzzy = geoGrouped['city']

#text mining function with threshold 
def compare_cities(query):
    #import pdb; pdb.set_trace()
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

#merge with the GeoData + drop missing values 
dfGrouped = dfTransform.groupby('newCity').sum().reset_index().rename(columns={'newCity':'city'})
dfMerged = pd.merge(dfGrouped,geoGrouped,how='left', left_on='city',right_on='city').dropna()

#export to csv
dfMerged.to_csv('fmMapPpl_'+today_date+'.csv')
print ('\ndata successfully saved')