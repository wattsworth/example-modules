#!/usr/bin/python3

import argparse
from joule.models.pipes import LocalPipe
from joule.client import CompositeModule

from high_bandwidth_reader import HighBandwidthReader
from example_filter import ExampleFilter


class ExampleComposite(CompositeModule):
    """ Merge reader and filter into a single module:
                [reader -> filter]->
    """

    async def setup(self, parsed_args,
                    inputs, outputs):
        # 1.) create nested modules
        my_reader = HighBandwidthReader()
        my_filter = ExampleFilter()

        # 2.) create local pipes for interior streams
        pipe = LocalPipe(name="raw", layout="float32_1")

        # 3.) convert modules into tasks
        #  output is an interior stream (write-end)
        parsed_args = argparse.Namespace(rate=100)
        task1 = my_reader.run(parsed_args, pipe)
        #  raw is an interior stream (read-end)
        #  filtered is an exterior stream
        parsed_args = argparse.Namespace()
        task2 = my_filter.run(parsed_args,
                              {"raw": pipe},
                              {"filtered": outputs["filtered"]})

        # 4.) tasks are executed in the main event loop
        return [task1, task2]


def main():
    r = ExampleComposite()
    r.start()


if __name__ == "__main__":
    main()
