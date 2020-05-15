# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class StockindexPipeline:
    def process_item(self, item, spider):
        # print(item['title'])
        # print(item['link'])
        # print(item['time'])
        # print(item['jieshao'])
        return item


class JsonWithEncoding(object):
    '''
    自定义导出json文件
    '''
    def __init__(self):
        #使用codecs模块的打开方式，可以指定编码打开，避免很多编码问题
        self.file = codecs.open("D:\github\stockindex\output\output.json","w",encoding="utf-8")

    def process_item(self,item,spider):
        lines = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(lines)

        #注意别忘返回Item给下一个管道
        # return item
    def spider_closed(self,spider):
        self.file.close()
