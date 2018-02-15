# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThreeAnswerScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question_title = scrapy.Field()
    question_id = scrapy.Field()

    first_author_name = scrapy.Field()
    first_answer_other = scrapy.Field()
    first_answer_detail = scrapy.Field()

    second_author_name = scrapy.Field()
    second_answer_other = scrapy.Field()
    second_answer_detail = scrapy.Field()
    
    third_author_name = scrapy.Field()
    third_answer_other = scrapy.Field()
    third_answer_detail = scrapy.Field()

