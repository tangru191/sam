import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
安全行业事业部的beta.sam.gov数据采集

由于数据是由js加载的，选择selenium+webdriver的方式进行采集

本部分为采集附件内容代码

采取拼接url构造页码url，在页码页面通过rule获取全部文章的url，从而获取附件的内容
"""


class SamfileSpider(CrawlSpider):
    name = 'samfile'
    allowed_domains = ['beta.sam.gov']
    # 页码部分进行自己构造拼接
    pages = [i for i in range(401, 1001)]
    start_urls = []
    for page in pages:
        start_urls.append(
            'https://beta.sam.gov/search?keywords=guam&sort=-modifiedDate&index=opp&is_active=false&page=' + str(page))

    rules = (
        # 根据rule获取所有页码内的所有列表文章的url，并使用parse_item解析
        Rule(LinkExtractor(allow=r'.*?/opp/[a-z0-9]{32}/.*'), callback='parse_item'),
    )

    def parse_item(self, response):
        # 通过正则获取文章的id，使用获取到的文章id拼接附件下载的url，yield请求下载
        patter = re.compile(r'[a-z0-9]{32}')
        subject = response.url
        match = patter.search(subject)
        raw_url_id = match.group(0)
        file_urls = 'https://beta.sam.gov/api/prod/opps/v3/opportunities/' + str(
            raw_url_id) + '/resources/download/zip?api_key=null&token='
        yield scrapy.Request(file_urls, callback=self.parse_zip, dont_filter=True)

    def parse_zip(self, response):
        # 附件下载完成以后提示附件下载成功
        print("附件下载成功！")
