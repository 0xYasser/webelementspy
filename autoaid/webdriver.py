from selenium import webdriver
import platform
import pathlib as path

_browsers = {
    **dict.fromkeys(['chrome','chromedriver'],'chromedriver'), 
    **dict.fromkeys(['firefox', 'ff', 'geckodriver'], 'geckodriver'),
    **dict.fromkeys(['safari'], 'safari')
    }
_os_map = {'Linux':'linux', 'Darwin':'mac', 'Windows':'win'}

_MAC_SAFARI_DRIVER_PATH = '/usr/bin/safaridriver'



class WebDriver():
    def __init__(self, browser):
        self.driver = self._web_driver(browser)

    def _web_driver(self, brw):
        browser = self._identify_browser(brw.lower())
        exe_path = self._find_executable_path(browser)
        kwargs = {'executable_path':exe_path}
        driver = None

        if browser == 'chromedriver':
            driver = self._chrome(**kwargs)
        elif browser == 'geckodriver':
            driver = self._firefox(**kwargs)
        elif browser == 'safari':
            driver = self._safari(**kwargs)
        return driver

    def _identify_browser(self, brw):
        try:
            return _browsers[brw]
        except KeyError:
            raise TypeError(f'not supported browser ({brw})')

    def _find_executable_path(self, brw):
        os = self._find_os()
        if os == 'mac' and brw == 'safari':
            return _MAC_SAFARI_DRIVER_PATH
        else:
            return path.PurePath('../drivers', os, brw)

    def _find_os(self):
        os_id = platform.system()
        try:
            return _os_map[os_id]
        except KeyError:
            raise TypeError(f'not supported OS ({os_id})')

    def _chrome(self, **kwargs):
        return webdriver.Chrome(**kwargs)

    def _firefox(self, **kwargs):
        return webdriver.Firefox(**kwargs)

    def _safari(self, **kwargs):
        return webdriver.Safari(**kwargs)
