# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from jobs.items import WyJobItem

class WyJobSpider(Spider):
    keywords = '翻译'
    name = 'wyjob'
    start_urls = [
        "http://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%25BF%25BB%25E8%25AF%2591,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=01&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    ]
    url1 = 'http://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%25BF%25BB%25E8%25AF%2591,2,'
    url2 = '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=01&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    totalPage = 1044
    def parse(self, response):
        sel = Selector(response)
        print('start!')
        for jobItems in sel.xpath('//*[@id="resultList"]/div[@class="el"]'):
            nextUrl = str(jobItems.xpath('p/span/a/@href').extract_first()).strip()
            if nextUrl != '' :
                print('url: '+nextUrl)
                yield Request(str(nextUrl), callback=self.parseDetail)

    def parseDetail(self, response):
        sel = Selector(response)
        item  = WyJobItem()
        item['url'] = response.url
        #print('url: '+ response.url)
        # /html/body/div[2]/div[2]/div[3]/div[1]/div/div/span[1] /html/body/div[2]/div[2]/div[3]/div[1]/div/div/span[2]/text()
        job_infobox_str = ''
        pix = ''
        i = 1
        for job_infobox in sel.xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/div/span'):
            print(job_infobox)
            if job_infobox_str != '':
                pix = '|'
            #job_infobox_str = job_infobox_str.join(pix+str(job_infobox.xpath('text()').extract_first()))
            #print(job_infobox_str)
            if i == 3:
                break
            i += 1
        item['job_infobox'] = job_infobox_str
        item['company_name'] = sel.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/p[1]/a/text()').extract()
        item['company_nature'] = sel.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/p[2]/text()').extract()
        item['company_industry'] = sel.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/p[2]/text()').extract()
        item['district'] = sel.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/span/text()').extract()
        item['level_job'] = self.keywords
        item['secondary_position'] = sel.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/h1/text()').extract()
        #item.professional_field = ''
        item['job_nature'] = '全职'
        item['job_address'] = sel.xpath('/html/body/div[2]/div[2]/div[3]/div[5]/div/p/text()').extract()
        item['job_jd'] = sel.xpath('/html/body/div[2]/div[2]/div[3]/div[4]/div/text()').extract()
        yield item


