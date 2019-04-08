'''
    Author：Jojo Wei
    Date： 03/04/2019
    Function：To get the info of new movies in Shenzhen posted on Douban
    Version：1.0
'''

import scrapy
from bs4 import BeautifulSoup
import re


class DoubanSpider(scrapy.Spider):
    name = 'douban_movie'
    start_urls = ['https://movie.douban.com/cinema/later/shenzhen/']
    custom_settings = {'LOG_LEVEL' :  'ERROR'}

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        tags = soup.find_all('div', class_= re.compile('item mod'))
        for link  in tags:
            movie_name = link.contents[3].find_all('a')[0].get_text( )
            pic_url = link.contents[1].find_all('img')[0].get('src')
            print(movie_name, pic_url)