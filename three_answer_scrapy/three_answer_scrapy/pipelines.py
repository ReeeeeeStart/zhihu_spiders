# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ThreeAnswerScrapyPipeline(object):
    def process_item(self, item, spider):
    	with open('data.txt','a') as f:
    		f.write('--------------------------------------' + '\n')
    		f.write('问题标题：' + item['question_title'] + '\n')
    		f.write('问题ID：' + item['question_id'] + '\n')
    		f.write('********回答如下：********' + '\n')
    		f.write('>>>>第一个回答：' + '\n')
    		f.write('作者：' + item['first_author_name'] + '\n')
    		f.write(item['first_answer_other'] + '\n')
    		f.write(item['first_answer_detail'] + '\n')

    		f.write('>>>>第二个回答：' + '\n')
    		f.write('作者：' + item['second_author_name'] + '\n')
    		f.write(item['second_answer_other'] + '\n')
    		f.write(item['second_answer_detail'] + '\n')

    		f.write('>>>>第三个回答：' + '\n')
    		f.write('作者：' + item['third_author_name'] + '\n')
    		f.write(item['third_answer_other'] + '\n')
    		f.write(item['third_answer_detail'] + '\n')

    		f.write('*************************' + '\n')
    		f.write('--------------------------------------' + '\n')


    	return item
