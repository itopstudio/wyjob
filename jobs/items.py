# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WyJobAreaItem(scrapy.Item):
    areaCode = scrapy.Field()
    areaName = scrapy.Field()

class WyJobItem(scrapy.Item):
    url = scrapy.Field() #招聘页面链接
    #release_date = scrapy.Field() #发布日期
    job_infobox = scrapy.Field()
    company_name = scrapy.Field() #公司名称
    company_nature = scrapy.Field() #公司性质
    company_industry = scrapy.Field() #公司行业
    district = scrapy.Field() #地区
    level_job = scrapy.Field() #一级岗位
    secondary_position = scrapy.Field() #岗位具体名称
    #professional_field = scrapy.Field() #专业领域
    job_nature = scrapy.Field() #全职或兼职及其他
    #experience = scrapy.Field() #工作经验
    job_jd = scrapy.Field() #职位jd
    job_address = scrapy.Field()
    #education = scrapy.Field() #学历要求
    #qualification_certificate = scrapy.Field() #证书
    #language_skills = scrapy.Field() #语言能力
    #technical_ability = scrapy.Field() #专业技能
    #salary_upperlimit = scrapy.Field() #薪资上限
    #salary_lowerlimit = scrapy.Field() #薪资下限

