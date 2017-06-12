#!/usr/bin/env python
# -*- coding: utf-8 -*-

# url 管理器


class UrlManager(object):

    def __init__(self):
        # 待爬取的新url列表： set()自动去重。
        self.new_urls = set()
        # 已爬取的url列表
        self.old_urls = set()

    # 添加单个解析后提取的新url到到待爬取的url列表中
    def add_new_url(self, url):
        if url is None:
            return
        # 如果url即不再待爬取的url列表也不在已爬取的url别表中，将其添加到带爬取的url列表中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 批量添加解析后提取的url到待爬取的url列表中
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        # 循环url列表，单个添加
        for url in urls:
            self.add_new_url(url)

    # 存在待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取一个待爬取的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

