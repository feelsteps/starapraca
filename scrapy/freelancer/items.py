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
    pass

class Person_Item(scrapy.Item):
    url = scrapy.Field()
    position = scrapy.Field()
    curr_status = scrapy.Field()
    name_company = scrapy.Field()
    location = scrapy.Field()
    education = scrapy.Field()
    hourly_daily_rate = scrapy.Field()
    languages = scrapy.Field()
    last_update = scrapy.Field()
    tags_list = scrapy.Field()
    skills = scrapy.Field()
    availability = scrapy.Field()
    other_info = scrapy.Field()
    pass