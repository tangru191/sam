# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SamItem(scrapy.Item):
    # 访问的url
    url = scrapy.Field()
    # 访问的title
    title = scrapy.Field()
    # 访问的文章html
    html = scrapy.Field()


class FileDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
