#!/usr/bin/python3

from joule import FilterModule, EmptyPipe
from scipy.signal import medfilt
import asyncio

WINDOW = 21
EDGE = (WINDOW-1)//2

class ExampleFilter(FilterModule):
    #Implement a WINDOW sized median filter
            
    async def run(self, parsed_args, inputs, outputs):
        raw = inputs["raw"]
        filtered = outputs["filtered"]
        while(1):
            #read new data
            try:
                vals= await raw.read()
            except EmptyPipe:
                break
            #execute median filter in place
            vals["data"] = medfilt(vals["data"],WINDOW)
            #write out valid samples
            await filtered.write(vals[EDGE:-EDGE])
            #prepend trailing samples to next read
            nsamples = len(vals)-2*EDGE
            if(nsamples>0):
                raw.consume(nsamples)
            #allow other routines to execute
            await asyncio.sleep(0.5)
            
if __name__ == "__main__":
    r = ExampleFilter()
    r.start()
