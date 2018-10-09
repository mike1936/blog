# Server:

import logging; logging.basicConfig(level=logging.INFO)
# Setting level to enable logging output in different place:
#     then use logging.info('test infomation') to replace print('test infomation')
# logging.debug(level=logging.DEBUG)
# logging.info(level=logging.INFO)
# logging.warning(level=logging.WARNING)
# logging.error(level=logging.ERROR)
import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body='<h1>Mike\'s blog</h1>', content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    site = '127.0.0.1'
    port = 9999
    srv = await loop.create_server(app.make_handler(), site, port)
    logging.info('Server started at http://%s:%s...' % (site, port))
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()