Example Modules
===============

*For more information read the Joule Documentation at*
http://docs.wattsworth.net/joule/writing_modules.html 

This repository contains reference implementations of a custom
FilterModule and ReaderModule.  Unittests for both modules are
included in the respective *_test.py files. Run the tests using
nose2:

.. code-block:: bash

		$> pip3 install nose2
		# ...output...
		$> cd example_modules
		$> nose2
		..
		------------------------------
		Ran 2 tests in 1.105s
		
		OK


This repository also contains an end-to-end test suite in the e2e
directory. This suite uses docker-compose to build a NilmDB and Joule
container for testing. See docker documentation for details on installing
docker compose: https://docs.docker.com/compose/

.. code-block::  bash

		 $> cd example_modules/e2e
		 $> ./runner.sh
		 # ...output from e2e setup ...
		 
		 # this is the e2e test output:
		 $> joule_1   | ---------[running e2e test suite]---------
		 $> joule_1   | OK
		 $> e2e_joule_1 exited with code 0
		 
		 # the rest of output is from e2e shutdown:
		 $> Aborting on container exit...
		 $> Stopping e2e_nilmdb_1 ... 
		 $> Going to remove e2e_joule_1, e2e_nilmdb_1
		 $> Removing e2e_joule_1 ... 
		 $> Removing e2e_nilmdb_1 ... 

		 
