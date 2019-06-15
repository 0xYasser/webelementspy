# -*- coding: utf-8 -*-
#pylint: disable=import-error

"""
webelementspy.spy.py
~~~~~~~~~~~~
This file contain spy functions 
:copyright: (c) 2019 by Yasser.
:license: MIT, see LICENSE for more details.
"""
import webdriver as wd
import jsscripts as js
import os

class Spy():
    def __init__(self, browser, url, executable_path=None):
        self.driver = wd.WebDriver(
            browser, executable_path=executable_path).driver
        self._navigate(url)
        self.init()

    def init(self):
        init_scripts = '\n'.join(s for s in js.js_init.values())
        self._execute(init_scripts)

    def capture(self):
        return self._execute_async(js.js_listner_capture)

    def close(self):
        self.driver.quit()

    def _navigate(self, url):
        self.driver.get(url)

    def _execute(self, script):
        self.driver.execute_script(script)

    def _execute_async(self, script):
        return self.driver.execute_async_script(script)

