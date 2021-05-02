import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')

# logger = logging.getLogger(__name__)
#
# # create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')
#
# # level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)
#
# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)
#
# logger.addHandler(stream_h)
# logger.addHandler(file_h)
#
# logger.warning('this is a warning')
# logger.error('this. is an error')

# config from file/dict

# import logging.config #####
# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger('simpleExample')
# logger.debug('this is a debug message')

try:
    a = [1,2,3]
    val=a[4]
except IndexError as e:
    logging.error(e, exc_info=True)

import traceback
try:
    b = [1,2,3]
    val = b[4]
except:
    logging.error('The error is %s', traceback.format_exc())


from logging.handlers import RotatingFileHandler


#RotateFileHandler enable create multi file logs
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)

# TimeRotatingHandler
# s, m, h ,d, midnight, w0, w6
# handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backcount=5)

#python-json-logger recommended