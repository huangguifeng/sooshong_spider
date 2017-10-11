# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #　公司名
    company_name = scrapy.Field()
    #　联系人
    contacts = scrapy.Field()
    # 电话
    telephone = scrapy.Field()
    # 手机号
    mobile_phone = scrapy.Field()
    # 传真
    fax = scrapy.Field()
    # 所在地区
    area = scrapy.Field()

    # 类型
    b_title = scrapy.Field()

    s_title =scrapy.Field()
