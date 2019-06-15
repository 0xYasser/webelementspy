import unittest, sys, pathlib
from webelementspy import webdriver as wd


class WebDriverTestCase(unittest.TestCase):

    def setUp(self):
        pass
    
    def test__init__chrome(self):
            wd.WebDriver('chrome', headless=True).driver.close()
    
    def test__init__firefox(self):
            wd.WebDriver('firefox', headless=True).driver.close()
    
    @unittest.skipUnless(sys.platform.startswith("darwin"), "requires MacOS")
    def test__init__safari(self):
            wd.WebDriver('safari').driver.close()

    def test_identify_browser(self):
        with self.assertRaises(NotImplementedError):
            wd.WebDriver._identify_browser(self,'NetScape')

        input_expected = {
            **dict.fromkeys(['chrome','chromedriver'],'chromedriver'), 
            **dict.fromkeys(['firefox', 'ff', 'geckodriver'], 'geckodriver'),
            **dict.fromkeys(['safari'], 'safari')
            }

        for case, expected in input_expected.items():
            actual = wd.WebDriver._identify_browser(self,case)
            self.assertEqual(expected, actual)

    def test_identify_os(self):
        with self.assertRaises(NotImplementedError):
            wd.WebDriver._identify_os(self,os='TampleOS')
        
        input_expected = {
            **dict.fromkeys(['Linux'],'linux'), 
            **dict.fromkeys(['darwin'], 'mac'),
            **dict.fromkeys(['Windows'], 'win')
            }

        for case, expected in input_expected.items():
            actual = wd.WebDriver._identify_os(self,case)
            self.assertEqual(expected, actual)

    def test_find_executable_path(self):
        with self.assertRaises(FileNotFoundError):
            wd.WebDriver._find_executable_path(self, 'NetScape','TampleOS')
            
        pathtype = pathlib.PurePosixPath if sys.platform in ('darwin', 'linux') else pathlib.PureWindowsPath
        input_expected = {
            **dict.fromkeys([('chromedriver','mac')], pathtype),
            **dict.fromkeys([('geckodriver','mac')], pathtype),
            **dict.fromkeys([('safari','mac')], pathtype)
            }

        for case, expected in input_expected.items():
            actual = type(wd.WebDriver._find_executable_path(self,*case))
            self.assertIs(expected, actual)



if __name__ == '__main__':
    unittest.main()