#!/usr/bin/env python3

from joule import FilterModule, EmptyPipe

class OffsetFilter(FilterModule):
    "Add offset to data "
    
    def custom_args(self, parser):
        grp = parser.add_argument_group("module","module specific arguments")
        grp.add_argument("--offset",
                         type=int,
                         required=True,
                         help="apply an offset")
        
    async def run(self, parsed_args, inputs, outputs):
        stream_in = inputs["input"]
        stream_out = outputs["output"]
        while(True):
            try:
                sarray = await stream_in.read()
                sarray["data"] += parsed_args.offset
                await stream_out.write(sarray)
                stream_in.consume(len(sarray))
            except EmptyPipe:
                break


def main():
    r = OffsetFilter()
    r.start()

if __name__ == "__main__":
    main()
