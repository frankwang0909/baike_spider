
## baike_spider

This a demo of python crawler

这个一个简单的爬虫示例。

## 爬取目标：

百度百科[Python词条](http://baike.baidu.com/item/Python)页面内的50个网页。


## 代码简单说明：

1.spider_main.py  

爬虫调度总程序

2.url_manager.py  

url管理器：用于管理url, 保存待爬取的url和已爬取的url列表。

3.html_downloader.py  

网页下载器：根据url，下载对应的网页

4.html_parser.py  

网页解析器：用于解析下载好的网页，提取需要的数据（比如词条标题和摘要，以及新的url)

5.html_outputer.py  

输出器：用于输出提取的数据，将提取的数据保存在本地html文件中。










