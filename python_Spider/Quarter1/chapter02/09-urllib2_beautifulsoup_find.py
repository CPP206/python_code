#-*- coding:utf-8 -*-
#09-urllib2_beautifulsoup_find.py

from bs4 import BeautifulSoup
import re

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


def hasClass_Id(tag):
	return tag.has_attr("class") and tag.has_attr("id")

soup = BeautifulSoup(html, "html.parser")

for child in soup.head.children:
	print(child)

for tag in soup.find_all(hasClass_Id):
	print tag.string
	

for child in soup.head.descendants:
	print(child)
