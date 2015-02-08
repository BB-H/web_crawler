import scrapy
import re
import urlparse
from caoliu_crawler.items import CaoliuItem
from scrapy.http import Request

class CaoliuSpider(scrapy.Spider):
    domainName = r'http://pw.pwcl.pw/'
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
		item['articleUrl'] = response.url
		
		title = response.xpath('//*[@id="main"]/div[4]/table/tr[1]/th[2]/table/tr/td/h4/text()')[0].extract().encode("utf-8")
		item['title'] = title
		print "Article title:", title
		
		articleDate = response.xpath('//*[@id="main"]/div[4]/table/tr[2]/th/div/text()')[1].re(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}')[0].encode("utf-8")
		item['articleDate'] = articleDate;
		print "DATE>>", articleDate
		
		torrentUrl = response.xpath('//*[@id="main"]//a[contains(.,"http://www.rmdown.com/link.php?hash")]/text()').extract()[0].encode('utf-8')
		item['torrentUrl'] = torrentUrl
		
		tempImgUrls = response.xpath('//*[@id="main"]/div[4]/table/tr[1]/th[2]/table/tr/td/div[4]//img/@src').extract();
		image_urls = []
		for img in tempImgUrls:
			img = img.encode("utf-8")
			if(img.endswith(".jpg") or img.endswith(".JPG")):
				img = img.replace('_thumb','')
				image_urls.append(img)
				if(len(image_urls)>9):
					break
		item['image_urls'] = image_urls
		yield item
		
		
		
		