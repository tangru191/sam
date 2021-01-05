import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ChinatopicSpider(CrawlSpider):
    name = 'chinaTopic'
    allowed_domains = ['rand.org']
    start_urls = ['https://www.rand.org/topics/china.html?page=']

    rules = (
        Rule(LinkExtractor(allow=r'china.html?page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
