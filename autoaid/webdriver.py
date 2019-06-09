import sys
import pathlib
from selenium import webdriver

_browsers = {
    **dict.fromkeys(['chrome','chromedriver'],'chromedriver'), 
    **dict.fromkeys(['firefox', 'ff', 'geckodriver'], 'geckodriver'),
    **dict.fromkeys(['safari'], 'safari')
    }
_os_map = {'Linux':'linux', 'darwin':'mac', 'Windows':'win'}

_MAC_SAFARI_DRIVER_PATH = '/usr/bin/safaridriver'



class WebDriver():
    def __init__(self, browser, headless = False):
        self.driver = self._web_driver(browser, headless)

    def _web_driver(self, brw, headless):
        browser = self._identify_browser(brw)
        os = self._identify_os()
        exe_path = self._find_executable_path(browser, os)
        kwargs = {'executable_path':exe_path}
        
        if browser == 'chromedriver':
            if headless:
                options = webdriver.ChromeOptions()
                options.headless = True
                kwargs['options'] = options
            driver = self._chrome(**kwargs)

        elif browser == 'geckodriver':
            if headless:
                options = webdriver.FirefoxOptions()
                options.headless = True
                kwargs['options'] = options
            driver = self._firefox(**kwargs)

        elif browser == 'safari':
            driver = self._safari(**kwargs)

        return driver

    def _identify_browser(self, brw):
        try:
            return _browsers[brw.lower()]
        except KeyError:
            raise NotImplementedError(f'not supported browser ({brw})')
    
    def _identify_os(self, os = None):
        os_id = sys.platform if not os else os
        try:
            return _os_map[os_id]
        except KeyError:
            raise NotImplementedError(f'not supported OS ({os_id})')

    def _find_executable_path(self, brw, os):
        exe_path = None
        if os == 'mac' and brw == 'safari':
            exe_path = pathlib.PurePath(_MAC_SAFARI_DRIVER_PATH)
        else:
            abs_path = pathlib.Path(__file__).resolve().parents[1] 
            drivers_path = abs_path / 'drivers'
            exe_path = pathlib.PurePath(drivers_path / os / brw)

        if pathlib.Path(exe_path).is_file():
            return exe_path
        else:
            raise FileNotFoundError(f'cannot find driver at {exe_path}')

    def _chrome(self, **kwargs):
        return webdriver.Chrome(**kwargs,)

    def _firefox(self, **kwargs):
        return webdriver.Firefox(**kwargs)

    def _safari(self, **kwargs):
        return webdriver.Safari(**kwargs)

