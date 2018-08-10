# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from html_sanitizer import Sanitizer
import re
#import logging

class FreelancermapDePipeline(object):
    def process_item(self, item, spider):
        return item


class DuplicatesPipeline(object):
    def __init__(self):
        self.urls_seen = set()
        
    def process_item(self, item, spider):
        if item['url'] in self.urls_seen:
            raise DropItem("Duplicate item found: %s" % item)
            #logging.log(logging.DEBUG, 'dupplicate item for person: ' + str(item['person_url']) + ' was dropped')
        else:
            self.urls_seen.add(item['url'])
            return item


class DataCleaningPipeline(object):
    '''
    cleaning columns: languages, education, hourly_daily_rate, skills, other_info, availability 
    from headers, empty rows, multiple spaces and html tags
    '''
    def process_item(self, item, spider):
        
        if spider.name != 'these_people':
            return item
        
        sanitizer = sanitizer = Sanitizer({'empty': {'h1', 'h2', 'h3', 'strong','em', 'p', 'ul', 'ol', 'li','br', 'sub', 'sup', 'hr', 'a'},
                                           'separate': set()})

        if (item['languages'][0] == 'Sprachkenntnisse:'):
            item['languages'] = item['languages'][1:]
        if (item['education'][0] == 'Abschluss:'):
            item['education'] = item['education'][1:]
        if (item['hourly_daily_rate'][0] == 'Stunden-/Tagessatz:'):
            item['hourly_daily_rate'] = item['hourly_daily_rate'][1:]
            
        h_d_rate = ' '.join(item['hourly_daily_rate'])
        h_d_rate = re.sub(' +|\n', '|', h_d_rate).split('|')
        
        item['hourly_daily_rate'] = list(filter(None, [i.strip() for i in h_d_rate if i]))
        item['languages'] = ''.join(item['languages']).split('|')
        item['skills'] = sanitizer.sanitize(''.join(item['skills']))
        item['other_info'] = sanitizer.sanitize(''.join(item['other_info']))
        item['availability'] = sanitizer.sanitize(''.join(item['availability']))
        return item