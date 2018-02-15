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
>>一般不用登录的网页，爬取的时候直接把网页的链接当成request就可以，比较简单。而现在要提取的是首页的问题，那么首先必须得先登录，即spider_name.py文件中申请的request是包含了你的登录信息的。而request中的登录信息就是浏览器的cookies，那这个cookies在哪呢？<br>
>>首先打开一个浏览器并登录你的知乎账号，然后按F12，右上角点击Application，找到左边一栏的Cookies，它就包含了你的登录信息.（用的是Chrome浏览器）<br>
>>可以发现cookies就是一个字典（Name当成key），我们把它全部都复制下来放到一个字典里面。<br>
>>之后return scrapy.Request() 时把cookies放进去就可以。<br>
>>知乎的模拟登录问题，网上有挺多总结的，直接复制浏览器的cookis应该是最简单粗暴的了。<br>

其他详细总结
-----------
[博客地址](http://blog.csdn.net/reeeeeestart/article/details/79327359)
