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
![](https://wx2.sinaimg.cn/large/005vjaOdgy1foh7vjm38jj30jr0cbta0.jpg)

>>可以发现cookies就是一个字典（Name当成key），我们把它全部都复制下来放到一个字典里面。<br>
>>之后return scrapy.Request() 时把cookies放进去就可以。<br>
>>知乎的模拟登录问题，网上有挺多总结的，直接复制浏览器的cookis应该是最简单粗暴的了。<br>

其他详细总结
-----------
[博客地址](http://blog.csdn.net/reeeeeestart/article/details/79327359)

新爬虫更新
---------
新爬虫，回答原本首页只有一个回答的疑问。<br>
为什么问题首页只解析出了一个回答的解释：<br>

>>首页中所包含的问题的request（链接）所生成的response里面只包含了一个回答（soup.prettify()打印后发现）。
>>但是平时我们从首页中点击相应的问题链接，进入具体问题的页面却发现有3个回答（多出来的两个回答上面显示“更多回答”）。
>>多次尝试后发现，进入具体问题的页面，其实一开始只有一个答案，但是很快知乎会动态加载出其他两个回答，所以平时我们从知乎首页进入相应问题页面是会出现三个回答。

那么如何获得问题首页的那3个回答？那就要弄清知乎是怎么动态加载出其他两个回答。

多次打开知乎首页并进入相应问题首页后，从浏览器提交的请求中发现headers的Request URL:
![](https://wx3.sinaimg.cn/large/005vjaOdgy1foh7eadgg1j30sh0almz3.jpg)
Request URL:https://www.zhihu.com/api/v4/questions/19616066/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=&limit=3&sort_by=default

里面有两个参数 一个是offset=&limit=3

参考师兄的博客，当offset=0，limit=3时，浏览器会提交3个回答的请求，多次尝试后发现这3个回答就是从首页进入相应问题后出现的3个回答。

之后，用json.loads 解析返回的json数据。
[‘data’][‘excerp’]是回答的前面一部分的摘要，把[data]字典打印（用pprint（））出来后发现：
>>content里面包含了全部的回答，但是里面包含了标签信息，所以不能直接以[‘data’][‘content’]的值作文为回答的全部内容，用get_text方法的话，回答的换行又处理不来，后来尝试用正则表达式想去删除里面的标签信息，试了好久后发现太难去除了。。。最后回到了用BeautiSoup库来解析content的字符串（有标签可以看成html）用soup.get_text('\n','</p\>')方法成功解决了换行问题。

最后输出到txt文件的效果：
![](https://wx2.sinaimg.cn/large/005vjaOdgy1foh7qjp0hhj30v20u043f.jpg)
