import time
# coding:utf-8
from urllib.parse import urljoin

import scrapy
import io
import sys

from sam00.items import Sam00Item

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


class Sam001Spider(scrapy.Spider):
    name = 'military'
    allowed_domains = ['www.military.com']
    start_urls = ['https://www.military.com/base-guide/browse-by-location']

    def parse(self, response):
        item = Sam00Item()
        states_xpath = response.xpath('//*[@id="paragraph-29481"]/div/div/div/ul/li')
        for state_xpath in states_xpath:
            # 美国军事基地所在地
            state = state_xpath.xpath('./h5/text()').get()
            # 美国军事基地名称 列表
            military_bases = state_xpath.xpath('./ul/li/a/text()').getall()
            # 美国军事基地 url  列表
            military_base_urls = state_xpath.xpath('./ul/li/a/@href').getall()
            for military_base, military_base_url in zip(military_bases, military_base_urls):
                item['state'] = state
                item['military_base'] = military_base
                item['military_base_url'] = military_base_url
                yield scrapy.Request(urljoin(response.url, military_base_url), meta={'item': item}, callback=self.parse_detail, dont_filter=True)
        print(item)

    def parse_detail(self, response):

        item = response.meta['item']
        item = Sam00Item()
        url = response.url
        content = response.xpath('//*[@id="bodyContent"]/article/div/div/div[1]/div[2]/p[2]/text()').get()
        pic = response.xpath('')
        print(url)
        print(content)







