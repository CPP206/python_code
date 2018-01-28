# -*- coding:utf-8 -*-

import logging
import random

L = logging.getLogger('name')


# 定义一个函数，生成0-1000的随机数
def func():
	return random.randint(1, 1000)


class myLogger(logging.LoggerAdapter):
	# 继承LoggerAdapter,重写process，生成随机数添加到msg前面
	def process(self,msg, kwargs):
		return '(%d),%s'%(self.extra['name'](), msg), kwargs


# 函数对象放入到字典中传入
LA = myLogger(L, {'name':func})

# now,do some logging
LA.debug('some_logging_message')

