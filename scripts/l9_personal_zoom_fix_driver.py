# -*- coding:utf-8 -*-
import os
import unittest
import sys
from time import sleep

from custom_driver.custom_driver import CustomDriver
from appium import webdriver
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestL9(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['deviceName'] = 'iPhone 5s'
        desired_caps['app'] = PATH(
            '/Users/chenjinhua/git/appium_ios/app/AppForUITest/appForUITest/build/Debug-iphonesimulator/appForUITest.app'
        )
        self.driver = CustomDriver('http://localhost:4723/wd/hub', desired_caps)
        print 'setUp'

    def tearDown(self):
        if sys.exc_info()[0]:  # Returns the info of exception being handled
            self.driver.save_screenshot(self.id().split(".")[-1]+".png")
        self.driver.quit()
        print 'tearDown'

    def test_zoom_fix(self):
        # 查找元素 操作  校验
        self.driver.find_element_by_xpath("//UIAButton[@label='Gesture']").click()
        self.driver.find_element_by_accessibility_id("Image (Zoom and Pinch)").click()

        image = self.driver.find_element_by_accessibility_id("imageScrollView")

        self.driver.zoom(image, percent=150, steps=10)
        sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestL9)
    unittest.TextTestRunner(verbosity=2).run(suite)
