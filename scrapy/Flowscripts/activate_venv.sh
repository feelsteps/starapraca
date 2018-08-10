#!/usr/bin/env bash

#activate 'scrapyenv' for scrapy
source /home/hadoopuser/scrapy/scrapyenv/bin/activate
echo 'scrapyenv was activated!'
python /home/hadoopuser/scrapy/freelancermap/spiders/runSpiders.py
echo 'data was scraped, in one minute we will launch merging and deduplication process!'




