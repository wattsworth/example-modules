Example Modules
===============

*For more information read the Joule Documentation at*
http://docs.wattsworth.net/joule

Example Reader:
--------------
Read random data, this can be extended to support low bandwidth sensors (<1Hz).

Usage:

.. code-block:: bash

  $> ./example_reader.py
  #output to terminal

  #Isolated execution (jouled must be running)
  $> ./example_reader.py --module_config="module_configs/example_reader.conf" --stream_configs="stream_configs"

Example Filter:
---------------
Apply a median filter of fixed WINDOW size 

Usage:

.. code-block:: bash

  #Isolated execution (jouled must be running)
  $> ./example_reader.py --module_config="module_configs/example_filter.conf" --stream_configs="stream_configs"

  #Historic Isolated Execution (jouled must be running)
  $> ./example_reader.py --module_config="module_configs/example_filter.conf" --stream_configs="stream_configs"
     --start="yesterday" --end="today"

Example Composite:
------------------
Combine the example reader and filter into a single module


  $> ./example_composite.py
  #output to terminal

  #Isolated execution (jouled must be running)
  $> ./example_composite.py --module_config="module_configs/example_composite.conf" --stream_configs="stream_configs"

Other Modules
-------------

High Bandwidth Reader: produce sawtooth waveform with adjustable data rate. 

Offset Filter: add an adjustable offset to a stream


Testing
-------

*UNDER DEVELOPMENT*

  Unittests are
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

		 
