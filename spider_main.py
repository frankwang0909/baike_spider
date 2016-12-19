# coding:utf-8

# main 函数

import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        # url管理器
        self.urls = url_manager.UrlManager()
        # html下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 解析器
        self.parser = html_parser.HtmlParser()
        # 输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw {0:d} : {1:s}'.format(count, new_url)

                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break

                count += 1

            # 异常处理
            except:
                print 'craw failed'

        # 输出数据
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)