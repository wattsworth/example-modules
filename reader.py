from joule.utils.time import now as time_now
from joule.client import ReaderModule
import asyncio
import numpy as np


class ReaderDemo(ReaderModule):
    "Example reader: generates incrementing values at user specified rate"

    def __init__(self):
        super(ReaderDemo, self).__init__("Demo Reader")
        self.description = "one line: demo reader"
        self.help = "a paragraph: this reader does x,y,z etc..."
    
    def custom_args(self, parser):
        parser.add_argument("rate", type=float, help="period in seconds")
        
    async def run(self, parsed_args, output):
        count = 0
        while(1):
            await output.write(np.array([[time_now(), count]]))
            await asyncio.sleep(parsed_args.rate)
            count += 1

            
if __name__ == "__main__":
    r = ReaderDemo()
    r.start()
