# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SamfiledownloadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FileDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    file_urls = scrapy.Field()  # ָ���ļ����ص�����
    files = scrapy.Field()