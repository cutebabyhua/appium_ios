# -*- coding:utf-8 -*-
import os
import unittest
import sys

from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestL10(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['deviceName'] = 'iPhone 5s'
        desired_caps['browserName'] = 'safari'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print 'setUp'


    def tearDown(self):
        if sys.exc_info()[0]:  # Returns the info of exception being handled
            self.driver.save_screenshot(self.id().split(".")[-1]+".png")
        self.driver.quit()
        print 'tearDown'

    def test_webApp_simulator(self):

        self.driver.get("http://www.baidu.com")

        # 搜索框输入appium
        input = self.driver.find_element_by_xpath("//input[@name='word']")
        input.clear()
        input.send_keys("appium")
        sleep(2)

        # 点击百度一下
        baidu = self.driver.find_element_by_xpath("//button[@id='index-bn']")
        baidu.click()
        sleep(5)
        self.driver.save_screenshot("webApp_real_device_screenshot.png")

        self.assertTrue(self.driver.find_element_by_name("Appium.io").is_displayed())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestL10)
    unittest.TextTestRunner(verbosity=2).run(suite)
