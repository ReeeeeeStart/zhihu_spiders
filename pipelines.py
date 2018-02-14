# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Python123DemoPipeline(object):
    def process_item(self, item, spider):

    	print('*************************')
    	with open('data.txt','a') as f:
    		f.write('--------------------------------------' + '\n')
    		f.write('问题标题：' + item['question_title'] + '\n')
    		f.write('问题详情：' + item['question_detail'] + '\n')
    		f.write('问题URL' + item['question_url'] + '\n')
    		f.write('作者：' + item['answer_author'] + '\n')
    		f.write(item['answer_voters'] + '\n')
    		f.write(item['answer_detail'] + '\n')
    		f.write('--------------------------------------' + '\n')
    	return item
