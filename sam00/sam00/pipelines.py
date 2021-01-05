# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# coding:utf-8
# useful for handling different item types with a single interface
import datetime

from sam00.TypeFolder.CnasType import CnasType


class Sam00Pipeline:
    def process_item(self, item, spider):
        return item


class ElasticsearchPipline(object):
    def process_item(self, item, spider):
        # 将item转化为es的数据
        cnas = CnasType()

        cnas.name = 'ThinkTanks-article'
        cnas.type = 'ThinkTanks'

        cnas.information = {
            "url": item["url"],
            "title": item["title"],
            "pub_time": item["pub_time"],
            "author": item["author"],
            "content": item["content"]
        }
        # cnas.date = datetime.datetime.now()
        cnas.user = "system"
        cnas.date = datetime.datetime.now().strftime('%F %T')
        cnas.save()
        return item


class MilitaryPipline(object):
    def process_item(self, item, spider):
        pass
