#!/usr/bin/env python3

from joule import FilterModule, EmptyPipe
from scipy.signal import medfilt
import asyncio


class ExampleFilter(FilterModule):
    """Apply linear scaling to input"""

    async def run(self, parsed_args, inputs, outputs):
        # data pipes (specified in configuration file)
        raw = inputs["raw"]
        scaled = outputs["scaled"]

        # linear scaling: y=mx+b
        m = 2.0
        b = 1.5

        while True:
            # read new data
            vals = await raw.read()
            # apply linear scaling y=mx+b
            vals["data"] = vals["data"] * m + b
            # write output
            await scaled.write(vals)
            # remove read data from the buffer
            raw.consume(len(vals))
            # propagate interval boundaries
            if raw.end_of_interval:
                await scaled.close_interval()
            # limit execution to 1Hz chunks
            await asyncio.sleep(1)


def main():
    r = ExampleFilter()
    r.start()


if __name__ == "__main__":
    main()
