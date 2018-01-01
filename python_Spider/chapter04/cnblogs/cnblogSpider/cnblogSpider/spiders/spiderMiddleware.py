import logging


###
class SpiderInputMiddleware(object):
    def process_spider_input(self, response, spider):
        logged.debug("#### 3333 response %s, spider %s ####"%(response, spider))
        return

class SpiderOutputMiddleware(object):
    def process_spider_output(self, response, result, spider):
        logged.debug("#### 4444 response %s, spider %s ####" %(response, spider))
        return result