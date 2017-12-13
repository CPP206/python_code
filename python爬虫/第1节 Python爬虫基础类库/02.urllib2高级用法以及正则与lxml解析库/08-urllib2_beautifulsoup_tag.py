#-*- coding:utf-8 -*-
#08-urllib2_beautifulsoup_tag.py

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#创建Beautiful Soup对象
soup = BeautifulSoup(html)

print soup.title
#<title>The Dormouse's story</title>

print soup.a
#<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>

print soup.p
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p>

print type(soup.p)
# <class 'bs4.element.Tag'>

print soup.name
#[document]  #soup对象本身比较特殊，它的name即为[document]

print soup.head.name
#head  #对于其他内部标签，输出的值便为标签本身的名称

print soup.p.attrs
#{'class':['title'], 'name':'dromouse'}
#在这里，我们把p标签的所有属性打印出来，得到的类型是一个字典

print soup.p['class']  #soup.p.get('class')
#['title']  #还可以利用get方法，传入属性的方法，二者是等价的。  

soup.a['class'] = 'newClass'
print soup.p   #可以对这些属性和内容等等进行修改
# <p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>

del soup.p['class']  #还可以对这个属性进行删除
print soup.p
# <p name="dromouse"><b>The Dormouse's story</b></p>

##NavigableString

print soup.p.string
# The Dormouse's story

print type(soup.p.string)
#<class 'bs4.element.NavigableString'>

##BeautifulSoup
print type(soup.name)
#<type 'unicode'>

print soup.name
#[document]

print soup.attrs #文档本身的属性为空

##Comment
print soup.a
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>

print soup.a.string
# Elsie 

print type(soup.a.string)
# <class 'bs4.element.Comment'>