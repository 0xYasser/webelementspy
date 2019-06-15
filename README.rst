======
WebelementSpy
======

Tool to identify web objects for automation written in Python

====
Install:
====
.. code-block:: bash

    $ git clone git@github.com:0xYasser/webelementspy.git
    $ cd webelementspy
    $ pip install -r requirements.txt


====
Usage:
====

there are two modes:
    1. onclick (default)
        will output ids only on clicked objects
    2. live
        will output ids on moseover events and on click event will output ids in different color

defaults:

.. code-block:: gherkin

        defaults = {'live': False, 'url': 'https://github.com',
            'browser': 'chrome', 'wp': (0, 0), 'ws': (898, 823), 'executable': None}

.. code-block:: bash

        $ cd webelementspy
        $ python spycli.py -h
        usage: spycli.py [-h] [-l] [-u URL] [-b BROWSER] [-e EXECUTABLE]

        spy on webpages to get id, xpath..etc for automation

        optional arguments:
          -h, --help            show this help message and exit
          -l, --live            show IDs on mouseover events
          -u URL, --url URL     initial navigate url
          -b BROWSER, --browser BROWSER 
                                specify browser to run
          -wp WINDOW_POSITION, --window-position WINDOW_POSITION
                                pecify brwoser window position
          -ws WINDOW_SIZE, --window-size WINDOW_SIZE
                                specify brwoser window size
          -e EXECUTABLE, --executable EXECUTABLE
                                    specify webdriver executable path

====
Run:
====
.. code-block:: bash

        $ cd webelementspy
        $ python spycli.py -l

.. image:: /docs/demo.gif

