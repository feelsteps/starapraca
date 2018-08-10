#C:/Users/filip.stepniak/Projects/1_Project_Leviathan/test_dataset/out/freelancermap/people/rfc_people_30-07-2018.json
import pandas as pd
import json
import itertools
import sys
import os
from datetime import datetime

today_date = datetime.today().strftime("%d_%m_%Y_%H_%M_%S")
#to do: rename dfs, provide path to jsonfiles and process them all;

#userinput of the path
userInput = input("Enter the path of your file: ")
assert os.path.exists(userInput), "I did not find the file "+str(userInput)

#load json file 
with open(userInput) as json_file:
    d = json.load(json_file)

#DataFrame from json file 
dfRead=pd.DataFrame(d)

dfCartProduct=[]
for i in dfRead['tags_list']:
    dfCartProduct.append(list(itertools.combinations(i,2)))

dfList = [item for sublist in dfCartProduct for item in sublist]

dfListSorted=[]
for i in dfList:
    dfListSorted.append(sorted(i))

dfCreated = pd.DataFrame(dfListSorted)
dfCreated.columns=['Source','Target']
dfCreated['Type']='Undirected'
dfSortedRenamed = dfCreated.groupby(['Source','Target','Type']).size().reset_index(name='Weight').sort_values(by=['Weight'], ascending=False).reset_index().drop(columns='index')

dfWeighted=dfSortedRenamed[dfSortedRenamed['Weight']>3]

#Exporting to .csv
#dfSortedRenamed.to_csv('row_gephi'+today_date+'.csv',index=False)
dfWeighted.to_csv('fmNetworkPpl_'+today_date+'.csv',index=False)
print ('\ndata successfully saved')