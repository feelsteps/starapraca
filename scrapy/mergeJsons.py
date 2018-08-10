# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:48:14 2018

@author: daulet.shamuratov
"""
import os
import json
import sys
from datetime import datetime
import re

def merge_Json_Files_In_Folder(inputFolder, outputFolder, additionalName):
    
    if (os.path.exists(inputFolder) and os.path.exists(outputFolder)):
        files = os.listdir(str(inputFolder))
        files = [x for x in files if x.endswith(".json")]
        head = []
        for json_file in files:
            with open(inputFolder + json_file, 'rb') as content: # open a single json file
                head.extend(json.load(content))
        print('all items: ' + str(len(head)))

        with open(outputFolder + "result_"+ additionalName +".json", "w") as outfile: #define output file
            json.dump(head, outfile, separators=(',', ': '), sort_keys=True)
    else:
        print("wrong path")


def remove_duplicates_In_Json(outputFolder, additionalName):
    
    checkpoint = outputFolder
    today_date = datetime.today().strftime('%d-%m-%Y-%H-%M-%S')
    new_json_name = "result_"+ today_date +".json"

    # check if result_additionalName.json is in folder
    if (os.path.exists(outputFolder) and os.path.isfile(outputFolder + "result_" + additionalName + ".json")):
        with open(outputFolder + "result_" + additionalName + ".json", 'rb') as content:
            data = json.load(content)
    	
        with open(outputFolder + new_json_name, "w") as outfile:
            all_urls = [record['url'] for record in data]
            unique_json = [data[all_urls.index(url)] for url in set(all_urls)]
            print('unique items: ' + str(len(unique_json)))
            json.dump(unique_json, outfile, sort_keys=True)
    else:
        print("wrong path")


if __name__ == '__main__':
    if len(sys.argv) == 4:
        merge_Json_Files_In_Folder(os.path.join(sys.argv[1], ""), os.path.join(sys.argv[2], ""), str(sys.argv[3]))
        remove_duplicates_In_Json(os.path.join(sys.argv[2], ""), str(sys.argv[3]))
    else:
        print("3 parameters are needed: inputFolder, outputFolder, additionalName")
        print("missing/wrong parameters for function: merge_Json_Files_In_Folder(inputFolder, outputFolder, additionalName)")
        print("missing/wrong parameters for function: remove_duplicates_In_Json(outputFolder, additionalName)")
        
        #remove_duplicates_In_Json("C:\\Users\\daulet.shamuratov\\freelancermap_de\\freelancermap_de\\files\\projects\\")
