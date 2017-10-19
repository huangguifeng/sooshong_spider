# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymysql import *

class ShSpiderPipeline(object):
    def process_item(self, item, spider):


        conn = connect(host='localhost', port=3306, user='root', password='mysql',
                       database='sooshang', charset='utf8')
        create_sql = "create table  If Not Exists sooshang.%s"%item['b_title'].encode('utf-8') + "(id int auto_increment primary key not null,company_name varchar(100) default '',contacts varchar(100) default '',telephone varchar(100) default '',mobile_phone varchar(100) default '',fax varchar(100) default '',area varchar(100) default '',stitle varchar(100) default '')"
        cs = conn.cursor()

        company_name = item['company_name'].encode('utf-8')
        # 　联系人
        contacts = item['contacts'].encode('utf-8')
        # 电话
        telephone = item['telephone'].encode('utf-8')
        # 手机号
        mobile_phone = item['mobile_phone'].encode('utf-8')
        # 传真
        fax = item['fax'].encode('utf-8')
        # 所在地区
        area = item['area'].encode('utf-8')

        s_title = item['s_title'].encode('utf-8')

        l = '"%s","%s","%s","%s","%s","%s","%s"'%(company_name,contacts,telephone,mobile_phone,fax,area,s_title)
        insert_sql =  "insert into %s"%item["b_title"].encode('utf-8') + " values(0,"+ l +");"
        print insert_sql
        cs.execute(create_sql)
        cs.execute(insert_sql)
        cs.close()
        conn.commit()
        conn.close()
        return item
