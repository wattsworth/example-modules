import asyncio
from aiohttp import web
from joule.client.reader_module import ReaderModule


class ExampleInterface(ReaderModule):

    async def run(self, parsed_args, output):
        # data processing...
        while True:
            await asyncio.sleep(1)

    def routes(self):
        return [web.get('/', self.index)]

    async def index(self, request):
        return web.Response(text="hello world!")


if __name__ == "__main__":
    r = ExampleVisualizer()
    r.start()
