# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Project_Item(scrapy.Item):
    proj_title = scrapy.Field()
    url = scrapy.Field()
    proj_type = scrapy.Field()
    start = scrapy.Field()
    duration = scrapy.Field()
    product_owner = scrapy.Field()
    location = scrapy.Field()
    publish_date = scrapy.Field()
    country = scrapy.Field()
    tags_list = scrapy.Field()
    text = scrapy.Field()
    
    '''
    whole_tag = scrapy.Field()
    tag_id = scrapy.Field()
    tag_href = scrapy.Field()
    '''