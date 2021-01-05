# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline


class SamPipeline:
    def process_item(self, item, spider):
        return item


# д��json�ļ�
class JsonWritePipline(object):
    def __init__(self):
        self.file = open('beta_sam_data(901-1000).json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
