#!/usr/bin/python3

from joule import ReaderModule
from joule.utilities import time_now
import asyncio
import numpy as np


class ExampleReader(ReaderModule):
    "Example reader: generates random values"
    
    async def run(self, parsed_args, output):
        while(1):
            value = np.random.rand()  # data from sensor
            await output.write(np.array([[time_now(), value]]))
            await asyncio.sleep(1)
            
if __name__ == "__main__":
    r = ExampleReader()
    r.start()
