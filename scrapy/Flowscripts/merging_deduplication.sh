#!/usr/bin/env bash

#this 3 cmd below starts pyScript to merge and deduplicate data with 2 inputs: inputFolder and outputFolder
python /home/hadoopuser/scrapy/mergeJsons.py /home/hadoopuser/scrapy/files/freelancermap/people/ /home/hadoopuser/scrapy/files/freelancermap/cmn_output people
sleep 10
python /home/hadoopuser/scrapy/mergeJsons.py /home/hadoopuser/scrapy/files/freelancermap/projects/ /home/hadoopuser/scrapy/files/freelancermap/cmn_output projects
