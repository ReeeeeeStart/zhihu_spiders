# -*- coding: utf-8 -*-
import scrapy
import re
import json
from bs4 import BeautifulSoup
from three_answer_scrapy.items import ThreeAnswerScrapyItem



class ThreeAnswerSpider(scrapy.Spider):          #以该名称为名的类，必须要继承scrapy.Spider类
    name = 'three_answer'
    allowed_domains = ['www.zhihu.com']    #要访问的网站的域名   

    headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
        } 
    cookies = {
      "_xsrf" : "你的cookies",
      "_zap" : "你的cookies",
      "aliyungf_tc" : "你的cookies",
      "capsion_ticket" : '你的cookies',
      "d_c0" : '你的cookies',
      "q_c1" : "你的cookies",
      "z_c0" : '你的cookies',
        }
    more_answer_url = 'https://www.zhihu.com/api/v4/questions/{0}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=3&sort_by=default'
    def start_requests(self):
        return [scrapy.Request("https://www.zhihu.com/",cookies = self.cookies,callback = self.after_login,headers = self.headers)]
    
    def after_login(self,response):
      print ('after login----------------------------------------')
      question_nums = re.findall(r'https://www.zhihu.com/question/(\d+)', response.text)
      for num in question_nums:
        three_answer_url = self.more_answer_url.format(num)
        yield scrapy.Request(three_answer_url, cookies = self.cookies,headers=self.headers, callback=self.parse)

    def parse(self,response):
      answers = json.loads(response.text)
      item = ThreeAnswerScrapyItem()
      i = 1
      item['question_title'] = answers['data'][0]['question']['title']
      item['question_id'] = re.match(r'http://www.zhihu.com/api/v4/questions/(\d+)', answers['data'][0]['question']['url']).group(1)
      for ans in answers['data']:
        if i == 1:
          item['first_author_name'] = ans['author']['name']
          item['first_answer_other'] = '点赞数：{0}  评论数：{1}'.format(ans['voteup_count'],ans['comment_count'])
          data = ans['content']
          soup = BeautifulSoup(data,"html.parser")
          item['first_answer_detail'] = soup.get_text('\n','</p>')
        if i == 2:
          item['second_author_name'] = ans['author']['name']
          item['second_answer_other'] = '点赞数：{0}  评论数：{1}'.format(ans['voteup_count'],ans['comment_count'])
          data = ans['content']
          soup = BeautifulSoup(data,"html.parser")
          item['second_answer_detail'] = soup.get_text('\n','</p>')
        if i == 3:
          item['third_author_name'] = ans['author']['name']
          item['third_answer_other'] = '点赞数：{0}  评论数：{1}'.format(ans['voteup_count'],ans['comment_count'])
          data = ans['content']
          soup = BeautifulSoup(data,"html.parser")
          item['third_answer_detail'] = soup.get_text('\n','</p>')
        
        i = i + 1
      return item