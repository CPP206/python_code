# -*- coding:utf-8 -*-
import logging

onelog = logging.LogRecord('name', '10', pathname=__file__, lineno=10, msg='hah', args=None, exc_info=None,func=None)
print onelog
print onelog.getMessage()

log_dict = {
	'name':'name',
	'levelno':'15',
	'lineno': '11',
	'msg': 'hehe',
	'pathname': __file__
}

secodlog = logging.makeLogRecord(log_dict)
print secodlog