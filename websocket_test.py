#coding:utf-8
import tornado.ioloop
import tornado.gen
from tornado.websocket import WebSocketHandler, websocket_connect, WebSocketError
import random
import logging
import time
import traceback
logger = logging.getLogger()
stream_hd = logging.StreamHandler()
log_format = logging.Formatter(
        '%(asctime)s %(name)s [%(levelname)s] [%(process)d] [%(filename)s:%(lineno)s] %(message)s',
        '%Y-%m-%dT%H:%M:%S')
stream_hd.setFormatter(log_format)
logger.addHandler(stream_hd)
logger.setLevel(logging.INFO)
IO_LOOP = tornado.ioloop.IOLoop.instance()
URL = 'ws://localhost:8000/thirdpart/session/pull'
URL = 'ws://10.103.14.48:10000/thirdpart/session/pull'
URL = 'ws://10.103.14.48:9999/thirdpart/session/pull'
BATCH = 5 
CONCURRENCE = 1500

@tornado.gen.coroutine
def main():
    
    try:
        ws_list = []
        for i in xrange(BATCH):
            start = time.time()
            new = yield [
                websocket_connect(URL, io_loop=IO_LOOP) for i in xrange(CONCURRENCE)
            ]
            ws_list.extend(new)
            logger.info('connected %s|cost %s' %(len(ws_list), time.time()-start))
#       logger.info('write message ...')
#       for i, ws in enumerate(ws_list):
#           ws.write_message('hello at %s' %i)
#           ws.write_message('hello again %s' %i)
#       logger.info('write message done')
    except:
        logger.error('error', exc_info=1)
    raise tornado.gen.Return(True)

if __name__ == '__main__':

    main()
    IO_LOOP.start()
