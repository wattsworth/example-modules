#!/usr/bin/env python3

from joule.client import ReaderModule
from joule.utilities import time_now
import asyncio
import numpy as np


class ExampleReader(ReaderModule):
    "Example reader: generates random values"

    async def run(self, parsed_args, output):
        while True:
            value = np.random.rand()  # data from sensor
            await output.write(np.array([[time_now(), value]]))
            await asyncio.sleep(1)


def main():
    r = ExampleReader()
    r.start()


if __name__ == "__main__":
    main()
