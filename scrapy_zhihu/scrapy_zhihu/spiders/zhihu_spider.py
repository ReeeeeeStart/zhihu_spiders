# -*- coding: utf-8 -*-

#引入要用到的库
import scrapy
import re
from bs4 import BeautifulSoup
from scrapy_zhihu.items import ScrapyZhihuItem #引入items.py文件中的ScrapyZhihuItem类，zhihu_spoder.py任务之一是要return item 这个item就是这个类的实例


class ZhihuSpiderSpider(scrapy.Spider):   #zhihu_spider是ZhihuSpiderSpider类的一个实例，下面定义了类的属性和方法。
    name = 'zhihu_spider'				  #注意：name，该爬虫的名字在整个项目中有且只能有一个、名字不可重复！name是spider最重要的属性，而且是必须的。		
    allowed_domains = ['www.zhihu.com']	  #这个不是必须的，但是在某写情况下需要用得到，比如使用爬取规则的时候就需要了；它的作用是只会跟进存在于allowed_domains中的URL。不存在的URL会被忽略。
#    start_urls = ['http://www.zhihu.com'] #命令行创建爬虫时默认生成的，可以不用。包含了Spider在启动时进行爬取的url列表。 

    headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
        } 
#登录用的cookis
    cookies = {
      "_xsrf" : "你的cookies",
      "_zap" : "你的cookies",
      "aliyungf_tc" : "你的cookies",
      "capsion_ticket" : '你的cookies',
      "d_c0" : '你的cookies',
      "q_c1" : "你的cookies",
      "z_c0" : '你的cookies',
        }
#初始化登录后的首页的request
    def start_requests(self):
        return [scrapy.Request("https://www.zhihu.com/",cookies = self.cookies,callback = self.get_questions_url,headers = self.headers)]

#获取首页的问题链接，并生成对应的request
    def get_questions_url(self,response):
      data = response.body
      soup = BeautifulSoup(data,"html.parser")
      for item in soup.find_all('a',attrs={'data-za-detail-view-element_name':"Title"}):
        if item['href'][1:9] == 'question' :  #首页中的链接还有专栏的文章，去掉这些链接
          question_url = "https://www.zhihu.com" + item['href']
          yield scrapy.Request(question_url,cookies = self.cookies,callback=self.parse,headers=self.headers)

#用BeautifulSoup解析response（问题页面）中的信息，并且return item  
    def parse(self,response):
      item = ScrapyZhihuItem()        #实例化ScrapyZhihuItem类
      soup = BeautifulSoup(response.body,"html.parser")
#所要信息的提取
      url = response.url
      answer = soup.find(class_='ContentItem AnswerItem')
      author_name = re.findall(r".*itemId",answer['data-zop'])[0][15:-9]
      question_title = soup.find('h1',class_='QuestionHeader-title').get_text()
      question_detail = soup.find('div',class_='QuestionHeader-detail').get_text()[0:-4]
      vote = soup.find_all('span',class_='Voters')
      answer_detail = soup.find('span',class_='RichText CopyrightRichText-richText').get_text('\n','</p>') #实现换行
#item字典的赋值
      item['question_title'] = question_title
      item['question_detail'] = question_detail
      item['question_url'] = url
      item['answer_detail'] = answer_detail
      item['answer_author'] = author_name
#赞同者这个信息有时候有，有时候没有      
      if len(vote) != 0:              #
        voters = vote[0].get_text()
        item['answer_voters'] = voters
      else:
        item['answer_voters'] = '无'
      
      return item
#首页中所包含的问题的request（链接）所生成的response里面只包含了一个回答（soup.prettify()打印后发现）。
#但是平时我们从首页中点击相应的问题链接，进入具体问题的页面却发现有3个回答（多出来的两个回答上面显示“更多回答”）
#多次尝试后发现，进入具体问题的页面，其实一开始只有一个答案，但是很快知乎会动态加载出其他两个回答。           