#-*- coding:utf-8 -*-

from logging import getLogger, StreamHandler, LoggerAdapter, basicConfig
import sys
import os
import random
L = getLogger('xxxx')
basicConfig(format='%(levelname)s:%(name)s:%(message)s')
L.setLevel('DEBUG')
L.debug('aa')

class myLogger(LoggerAdapter):
	def process(self, msg, kwargs):
		return '(%d),%s'%(self.extra['name1'](1,100), msg), kwargs

LA = myLogger(L, {'name1':random.randint})

LA.debug('haha')
LA.debug('hahha')