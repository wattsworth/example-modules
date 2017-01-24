from joule.utils.time import now as time_now
from joule.client import ReaderModule
import asyncio


class ReaderDemo(ReaderModule):
    "Example reader: generates an incrementing value every second"

    def __init__(self):
        super(ReaderDemo, self).__init__("Demo Reader")
        self.description = "one line: demo reader"
        self.help = "a paragraph: this reader does x,y,z etc..."
    
    def custom_args(self, parser):
        parser.add_argument("-o", "--optional", action="store_true",
                            help="custom arg")
    
    async def run(self, parsed_args, output):
        if(parsed_args.optional):
            print("option set")
        count = 0
        while(1):
            await output.write([[time_now(), count]])
            await asyncio.sleep(1)
            count += 1

            
if __name__ == "__main__":
    r = ReaderDemo()
    r.start()
