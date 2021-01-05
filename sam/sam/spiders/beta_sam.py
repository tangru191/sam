from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import io
import sys

from sam.items import SamItem, FileDownloadItem

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

"""
beta.sam.gov数据采集

由于数据是由js加载的，选择selenium+webdriver的方式进行采集

本部分为采集基本数据内容代码

采取拼接url构造页码url，在页码页面通过rule获取全部文章的url，从而获取附件的内容
"""


class BetaSamSpider(CrawlSpider):
    name = 'beta_sam'
    allowed_domains = ['beta.sam.gov']
    # 页码部分进行自己构造拼接
    pages = [i for i in range(901, 1001)]
    start_urls = []
    for page in pages:
        start_urls.append(
            'https://beta.sam.gov/search?keywords=guam&sort=-modifiedDate&index=opp&is_active=false&page=' + str(page))

    rules = (
        # 根据rule获取所有页码内的所有列表文章的url，并使用parse_item解析
        Rule(LinkExtractor(allow=r'.*?/opp/[a-z0-9]{32}/.*'), callback='parse_item'),
    )

    def parse_item(self, response):
        samitem = SamItem()
        # 访问的url
        samitem['url'] = response.url
        # 访问的title
        samitem['title'] = response.xpath('//*[@id="main-container"]/ng-component/page/div/div/div[3]/div[2]/div['
                                          '1]/h1/text()').get()
        # 访问的文章页面html
        samitem['html'] = [response.text]
        yield samitem
