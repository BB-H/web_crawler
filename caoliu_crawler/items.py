# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CaoliuItem(scrapy.Item):
	title = scrapy.Field()
	articleUrl = scrapy.Field()
	articleDate = scrapy.Field()
	#movieAlias = scrapy.Field()
	#torrent = scrapy.Field()
	torrentUrl = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()

