# -*- coding: utf-8 -*-

# Scrapy settings for caoliu_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'caoliu_crawler'

SPIDER_MODULES = ['caoliu_crawler.spiders']
NEWSPIDER_MODULE = 'caoliu_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'caoliu_crawler (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
	'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
	'caoliu_crawler.pipelines.MongoDBPipeline':300,
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "website_spider"
MONGODB_COLLECTION = "caoliu"

IMAGES_STORE = '/home/lei/caoliu_images'

IMAGES_MIN_HEIGHT = 320
IMAGES_MIN_WIDTH = 320

DOWNLOADER_MIDDLEWARES = {
	'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
	'caoliu_crawler.spiders.rotate_useragent.RotateUserAgentMiddleware' :400 
}

