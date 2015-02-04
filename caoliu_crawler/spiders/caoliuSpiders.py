import scrapy
import re
import urlparse
from caoliu_crawler.items import CaoliuItem
from scrapy.http import Request

class CaoliuSpider(scrapy.Spider):
    domainName = r'http://rm.enocr.com/'
    name = "caoliu"
    allowed_domains = ["rm.enocr.com","cl.clxxoo.com","pw.pwcl.pw","dz.pwcl.pw","cl.zrmv.org",]
    start_urls = [
        domainName+"thread0806.php?fid=15",
	 ]

    def parse(self, response):
		for sel in response.xpath('//tr/td/h3/a'):
			title = sel.xpath('text()').extract()
			if len(title)>0:
				title = title[0]
			else:
				title = ""
			subUrl = sel.xpath('@href').extract()
			if(len(subUrl)>0):
				subUrl = subUrl[0]
			else:
				subUrl = ""
			pattern = re.compile(r'\[.+\]')
			if(title and  subUrl and pattern.match(title) ):
				print "@@ %s ==>> %s" %(title, subUrl)
				yield Request(urlparse.urljoin(self.domainName, subUrl),self.parse_item)


    def parse_item(self,response):
		item = CaoliuItem()
		print "======== parse_item ======="