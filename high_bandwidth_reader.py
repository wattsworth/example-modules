#!/usr/bin/python3

from joule import ReaderModule, time_now
from joule import ReaderModule
import asyncio
import numpy as np


class HighBandwidthReader(ReaderModule):
    #Produce sawtooth waveform at specified rate"

    def custom_args(self, parser):
        grp = parser.add_argument_group("module",
                                        "module specific arguments")
        grp.add_argument("--rate", type=float,
                         required=True,
                         help=" output rate in Hz")
    async def run(self, parsed_args, output):
        start_ts = time_now()
        #run 5 times per second
        period=1
        samples_per_period=np.round(parsed_args.rate*period)
        while(1):
            end_ts = start_ts+period*1e6
            ts = np.linspace(start_ts,end_ts,
                             samples_per_period,endpoint=False)
            vals=np.linspace(0,33,samples_per_period)
            start_ts = end_ts
            await output.write(np.hstack((ts[:,None],
                                          vals[:,None])))
            await asyncio.sleep(period)
            
if __name__ == "__main__":
    r = HighBandwidthReader()
    r.start()
