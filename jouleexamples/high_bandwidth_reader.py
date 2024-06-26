#!/usr/bin/env python3

from joule.client import ReaderModule
from joule.utilities import time_now
import asyncio
import numpy as np


class HighBandwidthReader(ReaderModule):
    """ Produce a 1Hz ramp sampled at [rate] Hz """

    def custom_args(self, parser):
        grp = parser.add_argument_group("module",
                                        "module specific arguments")
        grp.add_argument("--rate", type=float,
                         required=True,
                         help="sample rate in Hz")

    async def run(self, parsed_args, output):
        start_ts = time_now()
        # run 5 times per second
        period = 1
        samples_per_period = np.round(parsed_args.rate * period)
        while True:
            end_ts = start_ts + period * 1e6
            ts = np.linspace(start_ts, end_ts,
                             samples_per_period, endpoint=False)
            vals = np.linspace(0, 33, samples_per_period)
            start_ts = end_ts
            chunk = np.hstack((ts[:, None], vals[:, None]))
            await output.write(chunk)
            await asyncio.sleep(period)


def main():
    r = HighBandwidthReader()
    r.start()

if __name__ == "__main__":
    main()
