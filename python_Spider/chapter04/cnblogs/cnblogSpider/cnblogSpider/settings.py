# -*- coding: utf-8 -*-

# Scrapy settings for cnblogSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'cnblogSpider'

SPIDER_MODULES = ['cnblogSpider.spiders']
NEWSPIDER_MODULE = 'cnblogSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cnblogSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#禁用Cookie
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#spider中间件
SPIDER_MIDDLEWARES = {
   # 'cnblogSpider.middlewares.CnblogspiderSpiderMiddleware': 543,
    'cnblogSpider.middlewares.ModifyStartRequest' : 643,
    'cnblogSpider.spiderMiddleware.SpiderInputMiddleware' : 743,
    'cnblogSpider.spiderMiddleware.SpiderOutputMiddleware': 843
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

#下载器中间件
#DOWNLOADER_MIDDLEWARES = {
#    'cnblogSpider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

#管道中间件
ITEM_PIPELINES = {
	# 'cnblogSpider.pipelines.CnblogJsonPipeline':10,
	# 'cnblogSpider.pipelines.CnblogspiderPipeline': 300,
 	# 'cnblogSpider.pipelines.CnblogspiderPipeline2': 100
 	# 'cnblogSpider.pipelines.TencentJsonPipeline' : 100
    # 'cnblogSpider.pipelines.SaveGirlImageItem' : 10
    'cnblogSpider.pipelines.MeizituPipelineJson' :10,
    'scrapy.pipelines.images.ImagesPipeline' : 1
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#是否遵循robot协议
ROBOTSTXT_OBEY = False

#设置日志等级
# LOG_LEVEL = "INFO"


IMAGES_STORE="/home/chenqi/python/python_code/python_Spider/chapter04/cnblogs/cnblogSpider/cnblogSpider/images"

IMAGES_URLS_FIELD = "image_urls"
IMAGES_RESULT_FIELD="images"