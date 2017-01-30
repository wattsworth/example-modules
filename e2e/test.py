import time
import numpy as np
import re
from joule.testing.e2eutils import joule
from joule.testing.e2eutils import nilmtool
import sys


def main():
    time.sleep(8)  # wait for jouled to boot and get data
    check_modules()
    check_data()
    check_logs()


def check_modules():
    """
    Test: check module status
    Goal:
      Demo Filter: running some nonzero memory
      Demo Reader: running some nonzero memory
    """
    modules = joule.modules()
    assert(len(modules) == 2)  # normal1,normal2,filter,broken
    for module in modules:
        title = module[joule.MODULES_TITLE_FIELD]
        status = module[joule.MODULES_STATUS_FIELD]
        if(title['name'] in ['Demo Filter', 'Demo Reader']):
            assert status == joule.MODULES_STATUS_RUNNING, "%s not running"%title
        else:
            assert(0)  # unexpected module in status report


def check_data():
    """
    Test: check data inserted into nilmdb
    Goal:
      /demo/raw is float32_1, has 1 interval with >50 samples
      /demo/filtered is float32_2, has 1 interval with >50 samples
      both filtered and raw have decimations
    """
    for path in ["/demo/raw", "/demo/filtered"]:
        # 1.) check streams have one continuous interval
        base_intervals = nilmtool.intervals(path)
        decim_intervals = nilmtool.intervals(
            path + "~decim-16")  # check level 2 decimation
        assert len(base_intervals) == 1,\
            "%s has %d intervals" % (path, len(base_intervals))
        assert len(decim_intervals) == 1,\
            "%s has %d intervals" % (path+"~decim-16", len(decim_intervals))
        # 2.) make sure this interval has data in it
        num_samples = nilmtool.data_count(path)
        assert(num_samples > 50)
        # 3.) make sure decimations have data
        assert(nilmtool.is_decimated(path, level=16, min_size=2))

    # verify stream layouts
    assert nilmtool.layout("/demo/raw") == "int32_1"
    assert nilmtool.layout("/demo/filtered") == "int32_1"

    # verify the filter module executed correctly
    # check the first 50 rows, the filter won't have
    # all the source data because the process was stopped
    expected_data = nilmtool.data_extract("/demo/raw")
    expected_data[:, 1:] += 2
    actual_data = nilmtool.data_extract("/demo/filtered")
    np.testing.assert_almost_equal(
        actual_data[:50, :], expected_data[:50, :])

    
def check_logs():
    """
    Test: logs should contain info and stderr from modules
    Goal:
      Demo Filter: says "starting" somewhere once
      Demo Reader: says "starting" somewhere once
    """
    for module_name in ["Demo Filter", "Demo Reader"]:
        logs = joule.logs(module_name)
        num_starts = len(re.findall(joule.LOG_STARTING_STRING, logs))
        assert(num_starts == 1)

        
if __name__ == "__main__":
    
    main()
    
    print("OK")

