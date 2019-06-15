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
usage:
====

.. code-block:: bash

        $ python spycli.py -h
        usage: spycli.py [-h] [-b BROWSER] [-e EXECUTABLE] [-u URL] [-l]

        spy on webpages to get id, xpath..etc for automation

        optional arguments:
        -h, --help            show this help message and exit
        -b BROWSER, --browser BROWSER
                        specify browser to run
        -e EXECUTABLE, --executable EXECUTABLE
                        specify webdriver executable path
        -u URL, --url URL     initial navigate url
        -l, --live            show IDs on mouseover events
