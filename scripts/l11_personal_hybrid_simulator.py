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
        desired_caps['app'] = PATH(
            '/Users/chenjinhua/git/appium_ios/app/app/AppForUITest/appForUITest/build/Debug-iphonesimulator/appForUITest.app'
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print 'setUp'


    def tearDown(self):
        if sys.exc_info()[0]:  # Returns the info of exception being handled
            self.driver.save_screenshot(self.id().split(".")[-1]+".png")
        self.driver.quit()
        print 'tearDown'

    def test_hybrid_simulator(self):

        # 进入 WebView 界面
        self.driver.find_element_by_xpath("//UIAButton[@name='WebView']").click()
        sleep(3)

        # 检查有没有 WebView Context
        if len(self.driver.contexts) == 1:
            raise AssertionError("can not find webView")

        # print(self.driver.contexts)
        # print(self.driver.current_context)

        # 切换到 WebView Context
        webView = self.driver.contexts[-1]
        self.driver.switch_to.context(webView)
        # print(self.driver.current_context)

        self.driver.find_element_by_link_text("点击后 testLabel 变成 abc").click()
        sleep(3)
        print(self.driver.current_context)

        # 切换到 Native Context
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element_by_xpath("//UIAButton[@name='OK']").click()
        print(self.driver.current_context)

        # print("WebView:\n%s" % self.driver.page_source)

        # 切换到 Native Context
        # self.driver.switch_to.context(self.driver.contexts[0])
        # print("Native:\n%s" % self.driver.page_source)
        self.assertEqual(self.driver.find_element_by_xpath("//UIAStaticText[@name='abc']").text, "abc")
        print(self.driver.current_context)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestL10)
    unittest.TextTestRunner(verbosity=2).run(suite)
