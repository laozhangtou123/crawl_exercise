import scrapy
import re
from ..items import XiaohuaItem
class XiaohuaSpider(scrapy.Spider):
    name="xiaohua"
    allowed_domains=['######']  #crawl beautiful girls
    start_urls=['#####']
    def parse(self, response):
        girls=response.xpath('//div[@class="img"]')
        for  girl in girls:
            item=XiaohuaItem()
            item['name']=girl.xpath('./span/text()').extract()[0]
            item['school']=girl.xpath('./div[@class="btns"]/a/text()').extract()[0]
            item['src'] = girl.xpath('./a[@target="_blank"]/img/@src').extract()[0]

            conpage=re.findall('(\d+)',response.url)[1]
            page=int(conpage)+1
            page='list-1-'+str(page)
            url=re.sub('list-1-\d+',page,response.url)
            yield item
            yield scrapy.Request(url,callback=self.parse)