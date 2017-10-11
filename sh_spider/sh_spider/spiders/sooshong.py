# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sh_spider.items import ShSpiderItem

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SooshongSpider(CrawlSpider):
    name = 'sooshong'
    allowed_domains = ['sooshong.com']
    start_urls = ['http://www.sooshong.com/']

    rules = (
        Rule(LinkExtractor(allow=r'company/$'), callback='parse_title',follow=True),
    )

    def parse_title(self,response):
        '''
            解析公司库
        :return:
        '''
        # 大类的名称
        b_title = response.xpath('//dt/a/text()').extract()
        # 大类url
        b_url = response.xpath('//dt/a/@href').extract()
        # 小类名称
        s_title = response.xpath('//dd/li/a/text()').extract()
        # 小类url
        s_url = response.xpath('//dd/li/a/@href').extract()


        for b in b_title:
            for i in range(len(s_title)):
                items = ShSpiderItem()
                items['b_title'] = b
                items['s_title'] = s_title[i]
                yield scrapy.Request('http://www.sooshong.com/'+ s_url[i],meta={'sooshang':items},callback=self.parse_item)


    def parse_item(self, response):
        '''
        列表页
        :param response:
        :return:
        '''
        items = response.meta['sooshang']
        # 列表页的公司ｕｒｌ
        c_url = response.xpath('//div[@class="title"]/a/@href').extract()

        #　其他列表页的ｕｒｌ
        o_url_list = response.xpath('//div[@class="page"]/a/@href').extract()
        # 排除不是页码不是ｕｒｌ。
        o_url = [i for i in o_url_list if i.startswith('/')]

        for c in c_url:
            #　发送公司请求详细页
            yield scrapy.Request(c,callback=self.parse_company,meta={'items':items})
        for o in o_url:
            #　发送其他页的请求
            yield scrapy.Request('http://www.sooshong.com/'+ o, callback=self.parse_item,meta={'sooshang':items})

    def parse_company(self,response):

        '''
        解析详细页的数据
        '''
        items = response.meta['items']
        if response.xpath('//div[@class="info_c"]//strong/text()') == []:
            return
        items['company_name'] = response.xpath('//div[@class="info_c"]//strong/text()').extract()[0]
        # 　联系人
        items['contacts'] =response.xpath('//div[@class="info_c"]/p/b/text()').extract()[0]
        # 电话
        items['telephone'] =response.xpath('//div[@class="info_c"]/p/text()')[0].extract()
        # 手机号
        items['mobile_phone'] =response.xpath('//div[@class="info_c"]/p/text()')[1].extract()
        items['fax'] = response.xpath('//div[@class="info_c"]/p/text()')[2].extract()
        # 所在地区
        items['area'] = response.xpath('//div[@class="info_c"]/p/text()')[10].extract()

        yield items

