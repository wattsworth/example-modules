Example Modules
===============

.. note::
   For more information read the Joule Documentation at
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


You may additionally want to run end-to-end tests using the jouled
process. The configuration directory contains an main.conf file and
corresponding stream and module configurations to run a local joule
instance. To automate this testing you can run the joule process in
Docker. See the e2e testing section in Joule for an example.

.. code-block::  bash

		 $> cd example_modules 
		 $> jouled -d e2e/main.conf &
		 $> joule -d e2e/main.conf modules
		 $> fg  # Ctrl-C to exit joule
		 
