# -*- coding: utf-8 -*-
#pylint: disable=import-error

"""
seleniumspy.spy.py
~~~~~~~~~~~~
This file contain spy functions 
:copyright: (c) 2019 by Yasser.
:license: MIT, see LICENSE for more details.
"""
import webdriver as wd
import jsscripts as js

class Spy():
    def __init__(self, browser, url):
        self.driver = wd.WebDriver(str(browser)).driver
        self._navigate(url)
        self.init()
        self.listen()

    def init(self):
        init_scripts = '\n'.join(s for s in js.js_init.values())
        self._execute(init_scripts)

    def listen(self):
        self._execute(js.js_start_listner)

    def capture(self):
        self._execute_async(js.js_listner_capture)

    def _navigate(self, url):
        self.driver.get(url)

    def _execute(self, script):
        self.driver.execute_script(script)

    def _execute_async(self, script):
        self.driver.execute_async_script(script)
