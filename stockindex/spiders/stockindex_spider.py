# -*- coding: utf-8 -*-
import scrapy
from ..items import StockindexItem

class StockindexSpiderSpider(scrapy.Spider):
    name = 'stockindex_spider'
    allowed_domains = ['www.cada.cn']
    # start_urls = ['http://www.cada.cn/Data/list_85_1.html']
    start_urls = ['http://www.cada.cn/Data/list_85_'+str(i)+'.html' for i in range(1,17)]

    def parse(self, response):
        # 遍历页面上所有//div[@class="neirong"]节点
        print(response.url)
        for stockitem in response.xpath('//div[@class="neirong"]'):
            item = StockindexItem()
            item['page'] = response.url
            item['title'] = stockitem.xpath('./a/text()').extract_first()
            item['link'] = stockitem.xpath('./a/@href').extract_first()
            item['time'] = stockitem.xpath('./div[@class="shijian"]/text()').extract_first().strip()
            item['jieshao'] = stockitem.xpath('./div[@class="jieshao"]/text()').extract_first().strip()
            yield item

        # # 提取下一页的li标签
        # next_url = response.xpath("//div[@class='fanye']/div[@class='p_tool']/a/text()").extract()[0]
        # # print("是否下一页的位置是%s" ,str(next_url))
        # # 提取待拼接的分页部分字符串
        # url_pae = response.xpath("//div[@class='fanye']/div[@class='p_tool']/a/text()").extract()
        # print(url_pae)
        #
        # if "下一页" in next_url:
        #     real_url = self.baseUrl + url_pae[0]
        #     print(real_url)
        #     yield scrapy.Request(real_url, callback=self.parse)
        # else:
        #     return
