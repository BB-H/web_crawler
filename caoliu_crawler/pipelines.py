# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import log
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

class CaoliuCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):
    def __init__(self):
		connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
		db = connection[settings['MONGODB_DB']]
		self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self,item,spider):
		title = item['title'] 
		articleDate = item['articleDate']
		#查找当前ITEM是否已经在数据库中存在，只有不存在时才入库
		matchedObj =  self.collection.find_one({'title':title,'articleDate':articleDate})
		if matchedObj:
			raise DropItem("The item is already existing in DB: [%s] %s" % (articleDate, title))
		else:
			self.collection.insert(dict(item))
			log.msg("Item wrote to MongoDB database %s/%s" %
					(settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
					level=log.DEBUG, spider=spider)
		return item