#!/usr/bin/env python3

from joule import ReaderModule
from joule.utilities import time_now
import asyncio
import numpy as np
import logging

ERROR_PROBABILITY = 0.25


class IntermittentReader(ReaderModule):
    """ Like HighBandwidth reader with random data interruptions """

    def custom_args(self, parser):
        grp = parser.add_argument_group("module",
                                        "module specific arguments")
        grp.add_argument("--rate", type=float,
                         required=True,
                         help="sample rate in Hz")

    async def run(self, parsed_args, output):
        start_ts = time_now()
        period = 1
        samples_per_period = np.round(parsed_args.rate * period)
        while True:
            try:
                end_ts = start_ts + period * 1e6
                ts = np.linspace(start_ts, end_ts,
                                 samples_per_period, endpoint=False)
                vals = np.linspace(0, 33, samples_per_period)
                start_ts = end_ts
                chunk = np.hstack((ts[:, None], vals[:, None]))
                # simulate an error
                if np.random.rand() < ERROR_PROBABILITY:
                    raise ValueError
                await output.write(chunk)
            except ValueError:
                logging.error("simulated data interruption")
                await output.close_interval()
            await asyncio.sleep(period)


def main():
    r = IntermittentReader()
    r.start()


if __name__ == "__main__":
    main()
