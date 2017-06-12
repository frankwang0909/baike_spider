#!/usr/bin/env python
# -*- coding: utf-8 -*-


class HtmlOutputer(object):

    def __init__(self):
        # 维护数据的列表
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    # 输出数据为html页面
    def output_html(self):

        # 新建文件对象
        f = open('output.html', 'w')
        f.write('<html><head><meta charset="utf-8"</head>')
        f.write('<body><table>')
        f.write('<thead><tr><td>url</td><td>title</td><td>summary</td></tr></thead>')
        f.write('<tbody>')
        
        for data in self.datas:
            f.write('<tr>')
            f.write('<td>%s</td>' % data['url'])
            f.write('<td>%s</td>' % data['title'].encode('utf-8'))
            f.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            f.write('</tr>')

        f.write('</tbody></table></body></html>')
        f.close()
