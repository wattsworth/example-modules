from joule.utils.localnumpypipe import LocalNumpyPipe
import asynctest
import asyncio
import numpy as np
import argparse
from filter import FilterDemo


class TestFilter(asynctest.TestCase):

    def test_filter(self):
        " with offset=2, output should be 2+input "
        # build test objects
        my_filter = FilterDemo()
        pipe_in = LocalNumpyPipe("input", layout="float32_1")
        pipe_out = LocalNumpyPipe("output", layout="float32_1")
        args = argparse.Namespace(offset=2)
        # create the input data 0,1,2,...,9
        # fake timestamps are ok, just use an increasing sequence
        test_input = np.hstack((np.arange(10)[:, None],   # timestamp 0-9
                                np.arange(10)[:, None]))  # data, also 0-9
        pipe_in.write_nowait(test_input)
        
        # run reader in an event loop
        loop = asyncio.get_event_loop()
        my_task = asyncio.ensure_future(
            my_filter.run(args,
                          {"input": pipe_in},
                          {"output": pipe_out}))
        
        loop.call_later(0.1, my_task.cancel)
        try:
            loop.run_until_complete(my_task)
        except asyncio.CancelledError:
            pass
        loop.close()
        # check the results
        result = pipe_out.read_nowait()
        # data should be 2,3,4,...,11
        np.testing.assert_array_equal(result['data'],
                                      test_input[:, 1]+2)
        # timestamps should be the same as the input
        np.testing.assert_array_almost_equal(result['timestamp'],
                                             test_input[:, 0])
