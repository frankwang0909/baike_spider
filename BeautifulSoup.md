

## 爬虫架构之网页解析器：

从网页中提取有价值数据的工具


## 解析的方式及工具

### 一、模糊匹配：正则表达式


### 二、结构化解析DOM: 

1.内置的 html.parser

2.第三方库 [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

3.第三方库 lxml

### BeautifulSoup
 
利用BeautifulSoup 来解析的步骤：

1.下载的html网页字符串 --> 2.创建BeautifulSoup对象 -->3.搜索节点find_all(), find() --> 4.访问节点、获取其名称、属性、文字等。


引入BeautifulSoup模块，给它取个简短的别名 bs

```python

from bs4 import BeautifulSoup as bs


html_doc = """<html><head><title>The Dormouse's story</title></head>
            <body>
            <p class="title"><b>The Dormouse's story</b></p>

            <p class="story" id="main">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
            and they lived at the bottom of a well.</p>

            <p class="story">...</p>
            """
```

创建BeautifulSoup对象


```python

soup = bs(html_doc, 'html.parser', from_encoding='utf-8')



print soup.prettify()
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story" id="main">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link2">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>

```

BeautifulSoup对象将HTML或者XML字符串解析为DOM树。

以下为常用的方法：

```
print soup.name
# [document]


# 标签对象，当做dictionary使用。
print soup.title
# <title>The Dormouse's story</title>

# 标签的name
print soup.title.name
# title

# 标签的属性
print soup.title.string
# The Dormouse's story

print soup.title.parent.name
# head

print soup.p   # print soup.find('p');
# <p class="title"><b>The Dormouse's story</b></p>

# 可以有多个值的属性是个list，比如'class'
print soup.p['class']
# [u'title']

print soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print soup.find_all('a')
# [
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# ]

print soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


# 提取url
for link in soup.find_all('a'):
    print(link.get('href'))

# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

# 提取文本
print soup.get_text()
# The Dormouse's story

# The Dormouse's story
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
# ...

# contents获得一个list
print soup.contents
# [<html><head><title>The Dormouse's story</title></head>\n<body>\n<p class="title"><b>The Dormouse's story</b></p>\n<p class="story">Once upon a time there were three little sisters; and their names were\n<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,\n<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and\n<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;\nand they lived at the bottom of a well.</p>\n<p class="story">...</p>\n</body></html>]

print len(soup.contents)
# 1

print soup.contents[0].name
# html

# children获取一个迭代器
for child in soup.find(id="main").children:
    print(child)
    
# Once upon a time there were three little sisters; and their names were
            
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# ,
            
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
#  and
            
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# ;
#             and they lived at the bottom of a well.

```