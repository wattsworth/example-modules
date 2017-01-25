from joule.client import FilterModule


class FilterDemo(FilterModule):
    " Example filter: applies a dc offset "

    def __init__(self):
        super(FilterDemo, self).__init__("Demo Filter")
        self.description = "one line: demo filter"
        self.help = "a paragraph: this filter does x,y,z etc..."
    
    def custom_args(self, parser):
        parser.add_argument("offset", type=float, default=0,
                            help="apply an offset")
        
    async def run(self, parsed_args, inputs, outputs):
        stream_in = inputs["input"]
        stream_out = outputs["output"]
        while(1):
            sarray = await stream_in.read()
            sarray["data"] += parsed_args.offset
            await stream_out.write(sarray)
            stream_in.consume(len(sarray))
            

if __name__ == "__main__":
    r = FilterDemo()
    r.start()
