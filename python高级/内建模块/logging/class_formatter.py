# -*- coding:utf-8 -*-

import logging

F = logging.Formatter(fmt='%(asctime)s:%(message)s:%(pathname)s:%(funcName)s')

oneLog = logging.LogRecord('name', '10', pathname=__file__, lineno=10, msg='haha', args = None, exc_info=None, func=None)

print F.format(oneLog)