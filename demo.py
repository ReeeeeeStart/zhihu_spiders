# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from pprint import pprint
import json


class DemoSpider(scrapy.Spider):           
    name = 'demo'
    allowed_domains = ['www.zhihu.com']    #   
    start_urls = ['http://www.zhihu.com'] 
    headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
        } 
#登录用的cookis
    cookies = {
      "_xsrf" : "204e9e85-ee81-4105-9531-b25dabd36351",
      "_zap" : "18e5599a-4e8a-44b8-83a7-13ca6a30133e",
      "aliyungf_tc" : "AQAAAIxDfh/mFw0ABWV8bi+nZCM6qH5i",
      "capsion_ticket" : '"2|1:0|10:1518403781|14:capsion_ticket|44:NWFlNDBjOTE0ZjVlNGNmMWFkYmU2ZjQ3MjAwYjU2YjQ=|81675f0aacafddf8311e1929e9cd5dd539ca0dcb6303fb529b91ac92e4829546"',
      "d_c0" : '"AIArj3sOIg2PTrI8uwZzbyQsAgtvkLKxkBw=|1518403797"',
      "q_c1" : "8a49a7dc25664e6ea76fe6c575ef21af|1518403779000|1518403779000",
      "z_c0" : '"2|1:0|10:1518403797|4:z_c0|80:MS4xZXg5dEFBQUFBQUFtQUFBQVlBSlZUZFZPYmxzQlFwT1lLNkhkSVg3dWN6VnV0THpuWUVqcmd3PT0=|b7ea7ecfcb3a3d94d3cbf51d33938be2778a9d3b5d5aa0857aea6dd400377efa"',
        }
#登录首页
    def start_requests(self):
        return [scrapy.Request("https://www.zhihu.com/",cookies = self.cookies,callback = self.get_questions_url,headers = self.headers)]
#获取首页的问题链接，去除掉专栏的文章链接
    def get_questions_url(self,response):
      print ('After Login----------------------------------------')
      data = response.body
      soup = BeautifulSoup(data,"html.parser")
      for item in soup.find_all('a',attrs={'data-za-detail-view-element_name':"Title"}):
        if item['href'][1:9] == 'question' :
          question_url = "https://www.zhihu.com" + item['href']
          print(question_url)
          yield scrapy.Request(question_url,cookies = self.cookies,callback=self.parse,headers=self.headers)
#处理提取到的问题的response
#并且先打印出来看是否成功提取   
    def parse(self,response):
      soup = BeautifulSoup(response.body,"html.parser")
      url = response.url
      question_title = soup.find('h1',class_='QuestionHeader-title').get_text()
      question_detail = soup.find('div',class_='QuestionHeader-detail').get_text()[0:-4]
      print('\n')
      print('--------------------------------------------------')
      print('问题：')
      print(question_title)
      print('问题详情：')
      print(question_detail)
      print('问题URL：')
      print(url)
#      print('\n--------------------------------------------------')
#      print(soup.prettify())
#      print('--------------------------------------------------\n')
      print('首页回答如下：')
      for item in soup.find_all(class_='ContentItem AnswerItem'):
        author_name = re.findall(r".*itemId",item['data-zop'])[0][15:-9]
        vote = soup.find_all('span',class_='Voters')

        answer_detail = soup.find('span',class_='RichText CopyrightRichText-richText').get_text('\n','</p>')
#        answer_detail = answer_detail.replace('<br>','\n')
#        answer_detail = answer_detail.replace('<p>','')
#        answer_detail = answer_detail.replace('</p>','\n')

        print('作者：' + author_name)
        if len(vote) != 0:
          voters = vote[0].get_text()
          print(voters)
        print(answer_detail)
      print('--------------------------------------------------')
      print('\n')



        
