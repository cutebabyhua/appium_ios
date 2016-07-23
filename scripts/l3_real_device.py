# -*- coding:utf-8 -*-
import os
import unittest

from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestiOSEnvironment(unittest.TestCase):
    def setUp(self):
        # open helloworld.app on iPhone 5 (7.0)
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3.1'
        desired_caps['deviceName'] = 'iPhone 5s'
        desired_caps['udid'] = '680d5b39d653ada092597393bf51e0947b0b368d'
        desired_caps['app'] = PATH(
            '/Users/chenjinhua/git/appium_ios/app/HelloWorld/DerivedData/HelloWorld/Build/Products/Debug-iphoneos/HelloWorld.app'
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print "setUp()"

    def tearDown(self):
        # end the session
        self.driver.quit()
        print "tearDown()"

    def test_screenshot(self):
        # wait for 5 seconds
        print "1"
        sleep(5)
        # take screenshot
        self.driver.save_screenshot("helloworld_screenshot.png")
        print "2"


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestiOSEnvironment)
    unittest.TextTestRunner(verbosity=2).run(suite)
