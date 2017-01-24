from joule.client import FilterModule


class FilterDemo(FilterModule):
    " Example filter: passes input to output "

    def __init__(self):
        super(FilterDemo, self).__init__("Demo Filter")
        self.description = "one line: demo filter"
        self.help = "a paragraph: this filter does x,y,z etc..."
    
    def custom_args(self, parser):
        parser.add_argument("-o", "--optional", action="store_true",
                            help="custom arg")
        
    async def run(self, parsed_args, inputs, outputs):
        stream_in = inputs["input"]
        stream_out = outputs["output"]
        if(parsed_args.optional):
            print("option set")

        while(1):
            sarray = await stream_in.read()
            await stream_out.write(sarray)
            stream_in.consume(len(sarray))
        
            
if __name__ == "__main__":
    r = FilterDemo()
    r.start()
