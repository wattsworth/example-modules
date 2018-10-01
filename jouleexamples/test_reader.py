from joule.utils.localnumpypipe import LocalNumpyPipe
import asynctest
import asyncio
import numpy as np
import argparse
from reader import ReaderDemo


class TestReader(asynctest.TestCase):

    def test_reader(self):
        " with a rate=0.1, reader should generate 10 values in 1 second "
        # build test objects 
        my_reader = ReaderDemo()
        pipe = LocalNumpyPipe("output", layout="float32_1")
        args = argparse.Namespace(rate=0.1, pipes="unset")
        # run reader in an event loop
        loop = asyncio.get_event_loop()
        my_task = asyncio.ensure_future(my_reader.run(args, pipe))
        loop.call_later(1, my_task.cancel)
        try:
            loop.run_until_complete(my_task)
        except asyncio.CancelledError:
            pass
        loop.close()
        # check the results
        result = pipe.read_nowait()
        # data should be 0,1,2,...,9
        np.testing.assert_array_equal(result['data'],
                                      np.arange(10))
        # timestamps should be about 0.1s apart
        np.testing.assert_array_almost_equal(np.diff(result['timestamp'])/1e6,
                                             np.ones(9)*0.1, decimal=2)
        
