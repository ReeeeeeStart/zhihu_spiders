Scrapy 爬取知乎首页问题及相应问题的首页回答
============================================
Power by
----------
>>1:Python 3.6.3<br>
>>2:beautifulsoup4 (4.6.0)<br>
>>3:Scrapy (1.5.0)<br>

如何使用
----------
>>首先将所需要的库安装好<br>
>>将scrapy_zhihu整个文件夹[下载](https://github.com/ReeeeeeStart/zhihu_spiders.git)下来。<br>
>>然后把整个文件夹放到一个目录下，如放到C盘中：C:\scrapy_zhihu。<br>
>>打开文件：C:\scrapy_zhihu\scrapy_zhihu\spiders\zhihu_spider.py，把自己登录知乎后的浏览器的cookies复制到文件中并保存。<br>
>>CMD进入你此文件夹（项目）的目录，如：cd C:\scrapy_zhihu。<br>
>>命令行输入命令：scrapy crawl zhihu_spider<br>
>>运行结束后，打开文件：C:\scrapy_zhihu\data.txt，里面存储的就是所提取的内容。<br>

模拟登录问题
----------
