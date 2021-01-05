# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class Sam00Item(scrapy.Item):
    state = scrapy.Field()
    military_base = scrapy.Field()
    military_base_url = scrapy.Field()


class CnasItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    pub_time = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()


# def save_to_es(self):
#     cnas_type = CnasType()
#     # lagou_type.url = self["url"]
#     cnas_type.url = self['url']
#     cnas_type.title = self['title']
#     cnas_type.pub_time = self['pub_time']
#     cnas_type.author = self['author']
#     cnas_type.content = self['content']
#     cnas_type.save()
#     return
