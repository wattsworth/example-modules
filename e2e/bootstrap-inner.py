#!/usr/bin/python3

import sys
import subprocess
import os
import signal

FORCE_DUMP = False


def main():
    jouled = subprocess.Popen(["jouled", "--config",
                               "/etc/joule/main.conf"],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              universal_newlines=True)
    print("---------[running e2e test suite]---------")
    sys.stdout.flush()
    test = subprocess.run(["python3", os.path.join("/etc/joule/test.py")])
    jouled.send_signal(signal.SIGINT)
    if(test.returncode != 0 or FORCE_DUMP):
        print("----dump from jouled----")
        stdout, _ = jouled.communicate()
        for line in stdout.rstrip().split('\n'):
            print("> %s" % line)
        return test.returncode

    
if __name__ == "__main__":
    exit(main())
