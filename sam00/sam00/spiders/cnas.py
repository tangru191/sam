#coding:utf-8
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from sam00.items import CnasItem
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class CnasSpider(CrawlSpider):
    name = 'cnas'
    allowed_domains = ['cnas.org']
    start_urls = ['https://www.cnas.org/articles-multimedia?area=defense']

    rules = (

        # # https://www.cnas.org/reports/p1?area=defense  报告部分的规则
        # Rule(LinkExtractor(allow=r'.*?p\d+\?area=defense'), follow=True),
        # # https://www.cnas.org/publications/reports/rethinking-requirements-and-risk-in-the-new-space-age
        # Rule(LinkExtractor(allow=r'https://www.cnas.org/publications/reports/[a-z0-9\-]+'), callback='parse_item',
        #      follow=False),

        # https://www.cnas.org/reports/p1?area=defense
        Rule(LinkExtractor(allow=r'.*?p\d+\?area=defense'), follow=True),
        # https://www.cnas.org/publications/reports/rethinking-requirements-and-risk-in-the-new-space-age
        Rule(LinkExtractor(allow=r'https://www.cnas.org/publications/commentary/[a-z\-]+'), callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):
        item = CnasItem()
        url = response.url

        title = response.xpath('//*[@id="content"]/article/header//h1/text()').get()
        pub_time = ''
        if 'Image credit:' in str(response.xpath('//*[@id="content"]/article/header/div/div[1]/p/text()').get()):
            pub_time = response.xpath('//*[@id="content"]/article/header/div[2]/div[1]/p[2]/text()').get()
        else:
            pub_time = response.xpath('//*[@id="content"]/article/header/div/div[1]/p/text()').get()


        author = ''
        if response.xpath('//*[@id="content"]/article/header/div/div/p/a/text()').get():
            author = response.xpath('//*[@id="content"]/article/header/div/div/p/a/text()').get()
        else:
            # response.xpath('//*[@id="content"]/article/header/div/div[3]/p/span[2]/text()').get():
            author = response.xpath('//*[@id="content"]/article/header/div/div[3]/p/span[2]/text()').get()

        content = ''
        if response.xpath('//*[@id="mainbar"]/div/p/text()'):
            content = response.xpath('//*[@id="mainbar"]/div/p/text()').getall()
        else:
            content = response.xpath('//*[@id="mainbar-toc"]/div/p/text()').getall()

        item["url"] = url
        item["title"] = title
        item["pub_time"] = pub_time
        item["author"] = author
        item["content"] = content
        return item
