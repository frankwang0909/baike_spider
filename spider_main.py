#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 爬虫总调度程序

import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    # 构造函数，初始化
    def __init__(self):
        # url管理器
        self.urls = url_manager.UrlManager()
        # 下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 解析器
        self.parser = html_parser.HtmlParser()
        # 输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, url):
        count = 1
        # 添加root_url到url管理器的urls
        self.urls.add_new_url(url)
        # 启动爬虫的循环
        while self.urls.has_new_url():
            try:
                # 获取待爬去的url
                new_url = self.urls.get_new_url()
                # 打印爬取的url
                print 'craw %d :%s' %(count, new_url)
                # 启动下载器下载网页
                html_cont = self.downloader.download(new_url)
                # 解析器解析网页和提取新的url
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 添加提取的新url列表到url管理器的url列表中
                self.urls.add_new_urls(new_urls)
                # 收集提取的网页内容
                self.outputer.collect_data(new_data)
                # 只爬前50个网页
                if count == 50:
                    break

                count += 1
            except:
                print 'craw failed'

        # 提取的内容
        self.outputer.output_html()

if __name__ == "__main__":
    # 入口url
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
