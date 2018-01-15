#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import datetime


r = requests.get("https://book.douban.com")

html = r.text  #text用作文本解析，如果爬取图片用content

soup = BeautifulSoup(html, 'html.parser')

items = []
global_van_items = soup.find('div', class_='global-nav-items')   #class比较特殊，使用class_

for tag in global_van_items:
	items.append(tag.string)   #这里区分beautifulsoup中的string与get_text()方法的区别

print(items)

class Info(object):
	def __init__(self, title, img, link, author, year, publisher, abstract):
		self.title = title
		self.img = img
		self.link = link
		self.author = author
		self.year = year
		self.publisher = publisher
		self.abstract = abstract

new_book_html = soup.find('ul', class_='list-col5 list-express slide-item')
book_info_list = []

for tag in new_book_html.find_all('li'):
	info_html = tag.find('div', class_ = 'info')
	info_title = info_html.find('a')
	title = info_title.string.strip()
	cover = tag.find('div', class_='cover')
	img = cover.find('img')['src'].strip()
	href = info_title['href'].strip()
	author = info_html.find(class_='author').string.strip()
	year = info_html.find(class_='year').string.strip()
	publisher = info_html.find(class_='publisher').string.strip()
	abstract = info_html.find(class_='abstract').string.strip()
	book = Info(title, img, href, author, year, publisher, abstract)
	book_info_list.append(book)

print('推荐%s本书'%len(book_info_list))

for book in book_info_list:
	print("*" * 100)
	print(book.title)
	print(book.img)
	print(book.link)
	print(book.author)
	print(book.year)
	print(book.publisher)
	print(book.abstract)

def save():
	today = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
	file_name = "豆瓣" + today + "推荐书单"
	with open(file_name +".md", "w") as file:
		file.write("# "+ file_name)
		file.write('\\n---')
	with open(file_name+'.md', 'a') as file:
		num = 1
		for book in book_info_list
			file.write('\n\\n')
			file.write('## ' + str(num) + '. '+book.title)
			file.write('\\n')
			file.write('!['+book.title +' cover img]('+ book.img+')')
			file.write('\n\\n')
			file.write('简介\\n')
			file.write('---\\n')
			file.write('')

if __name__ == "__main__":
	save()
