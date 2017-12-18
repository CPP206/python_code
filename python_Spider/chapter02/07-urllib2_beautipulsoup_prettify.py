#-×- coding:utf-8 -×-
#beautifulsoup4_test.py

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

#打开本地HTML文件的方式来创建对象
#soup = BeautifulSoup(open('index.html'))

#格式话输出soup对象的内容
print(soup.prettify())