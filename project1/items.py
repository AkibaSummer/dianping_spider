# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Project1Item(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    url = scrapy.Field()
    comment_num = scrapy.Field()
    avg_cost = scrapy.Field()
    taste = scrapy.Field()
    environment = scrapy.Field()
    service = scrapy.Field()
    food_type = scrapy.Field()
    location = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
