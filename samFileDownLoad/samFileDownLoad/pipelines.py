# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from os.path import join, basename, dirname
from urllib.parse import urlparse

from scrapy import Request
from scrapy.pipelines.files import FilesPipeline

from itemadapter import ItemAdapter


class SamfiledownloadPipeline:
    def process_item(self, item, spider):
        return item


class FileDownloadPipeline(FilesPipeline):
    # def process_item(self, item, spider):
    #     return item
    def get_media_requests(self, item, info):
        yield Request(item['file_urls'], meta={'name': item['name']})

    def file_path(self, request, response=None, info=None):  # �޸��ļ���
        filename = request.meta['name']
        return '%s' % filename
