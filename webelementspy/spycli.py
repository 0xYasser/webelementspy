# -*- coding: utf-8 -*-
#pylint: disable=import-error

'''
webelementspy.spycli
~~~~~~~~~~~~
This file contain command line interface functions 
:copyright: (c) 2019 by Yasser.
:license: MIT, see LICENSE for more details.
'''

from spy import Spy
import argparse
import json


defaults = {'live': False, 'url': 'https://github.com', 'browser': 'chrome',
            'executable': None}

class SpyCLI():
    def __init__(self, args):
        self.live = args.live if args.live else defaults['live']
        self.browser = args.browser if args.browser else defaults['browser']
        self.url = args.url if args.url else defaults['url']
        self.executable = args.executable if args.executable else defaults['executable']
        self.spyer = self.init_driver()
        self.main_loop()

    def main_loop(self):
        try:
            while True:
                output = json.loads(self.spyer.capture())
                if 'pyspy_error' in output:
                    self.spyer.init()
                    continue
                self.printer(output)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            raise e        
        finally:
            self.spyer.close()

    def init_driver(self):
        return Spy(self.browser, self.url, self.executable)

    def printer(self, text):
        data = self.output_handler(text)
        if data: print(data)
        
    def output_handler(self, args):
        if args['PATHS']:
            if self.live:
                if args['EVENT'] != 'click':
                    return (args['PATHS'])
                else:
                    return (self.make_green(args['PATHS']))
            else:
                if args['EVENT'] == 'click':
                    return (self.make_green(args['PATHS']))


    def make_green(self, text): 
        return f"\033[92m{text}\033[00m"
    


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='spy on webpages to get id, xpath..etc for automation')

  parser.add_argument(
      '-l', '--live', help='show IDs on mouseover events', action='store_true')
  parser.add_argument(
      '-u', '--url', help='initial navigate url', action='store')

  parser.add_argument(
      '-b', '--browser', help='specify browser to run', action='store')
  
  parser.add_argument(
      '-e', '--executable', help='specify webdriver executable path', action='store')

  args = parser.parse_args()

  SpyCLI(args)
