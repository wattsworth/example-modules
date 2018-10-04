#!/usr/bin/env python3

import asyncio
from aiohttp import web
import aiohttp_jinja2
import jinja2
import os
from random import randint

from joule.client.reader_module import ReaderModule

CSS_DIR = os.path.join(os.path.dirname(__file__), 'assets', 'css')
JS_DIR = os.path.join(os.path.dirname(__file__), 'assets', 'js')
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'assets', 'templates')


class BootstrapInterface(ReaderModule):

    async def setup(self, parsed_args, app, output):
        loader = jinja2.FileSystemLoader(TEMPLATES_DIR)
        aiohttp_jinja2.setup(app, loader=loader)

    async def run(self, parsed_args, output):
        # data processing...
        while True:
            await asyncio.sleep(1)

    def routes(self):
        return [
            web.get('/', self.index),
            web.get('/data.json', self.data),
            web.static('/assets/css', CSS_DIR),
            web.static('/assets/js', JS_DIR)
        ]

    @aiohttp_jinja2.template('index.jinja2')
    async def index(self, request):
        return {'message': "hello world"}

    # json end point for AJAX requests
    async def data(self, request):
        # return summary statistics, etc.
        return web.json_response(data={'random_value': randint(0, 10)})


def main():
    r = BootstrapInterface()
    r.start()


if __name__ == "__main__":
    main()
