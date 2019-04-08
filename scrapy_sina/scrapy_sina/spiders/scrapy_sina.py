'''
    Author：Jojo Wei
    Date： 08/04/2019
    Function：To get the info of Chinse news from Sina
    Version：1.0
'''


import scrapy
from bs4 import  BeautifulSoup
import re


class SinaNewsSpider(scrapy.Spider):
    name = 'sina_news'  # give the spider a name: sina_news 
    start_urls = ['http://news.sina.com.cn/']

    def parse(self, response): # parse the webpage
        soup = BeautifulSoup(response.body, 'lxml')
        tags = soup.find_all('a', href = re.compile(r'sina.*\d{4}-\d{2}-\d{2}.*shtml$'))

        # make sure only new link is included
        for tag in tags:
            print(tag.text, tag.get('href'))
