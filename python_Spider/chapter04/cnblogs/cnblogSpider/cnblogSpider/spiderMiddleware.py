import logging

logger = logging.getLogger(__name__)
###
class SpiderInputMiddleware(object):
    def process_spider_input(self, response, spider):
        logging.info("#### 3333 response %s, spider %s ####"%(response, spider))
        return

class SpiderOutputMiddleware(object):
    def process_spider_output(self, response, result, spider):
        logging.info("#### 4444 response %s, spider %s ####" %(response, spider))
        return result