#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        # 存储提取的url列表
        new_urls = set()

        # 正则匹配需要提起的词条url  /item/
        links = soup.find_all('a', href = re.compile(r"/item/\w+"))

        for link in links:
            new_url = link['href']

            # 拼接完整的url
            new_full_url = urlparse.urljoin(page_url, new_url)

            # 添加到url列表中
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        # 存储解析的数据
        res_data = {'url': page_url}

        # 搜索title节点
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        # print title_node.get_text()
        res_data['title'] = title_node.get_text()


        # 搜索summary节点
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        # print summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        # print soup.prettify()
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls, new_data