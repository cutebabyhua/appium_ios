# -*- coding:utf-8 -*-
import os
import unittest
import sys
from appium import webdriver

# Returns abs path relative to this file and not cwd
# os.path模块主要用于文件的属性获取
# os.path.abspath(path) //返回path规范化的绝对路径。
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# SCREENSHOT_NAME = "check_sum_error.png"

class TestAppiumIosL5(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "setUpClass"
        super(TestAppiumIosL5, cls).setUpClass()
        # open TestApp.app on simulator iPhone 5s (9.3)
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'

        # simulator
        desired_caps['deviceName'] = 'iPhone 5s'
        desired_caps['app'] = PATH(
            '/Users/chenjinhua/git/appium_ios/app/TestApp/DerivedData/TestApp/Build/Products/Debug-iphonesimulator/TestApp.app'
        )
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        super(TestAppiumIosL5, cls).tearDownClass()
        print 'tearDownClass'
        cls.driver.quit()


    def setUp(self):
        # clear screenshot

        if os.path.exists(SCREENSHOT_NAME):
            os.remove(SCREENSHOT_NAME)
        print 'setUp'

    def tearDown(self):

        # check if need to take screenshot
        if sys.exc_info()[0]:  # Returns the info of exception being handled
            self.driver.save_screenshot(self.id().split(".")[-1]+".png")
        print 'tearDown'
        # self.id()获取当前test_method完整的名字,脚本名.类名.方法名
        # split(".")[-1]以.为分隔符,取最后一个值

    def test_check_sum_function(self):
        first_arg = 5
        second_arg = 6

        # find elements
        first_arg_textfield = self.driver.find_element_by_accessibility_id("IntegerA")
        second_arg_textfield = self.driver.find_element_by_xpath("//UIATextField[@label='IntegerB']")
        sum_button = self.driver.find_element_by_name("ComputeSumButton")

        # compute sum
        # first_arg_textfield.send_keys("")
        first_arg_textfield.clear()
        first_arg_textfield.send_keys(str(first_arg))
        second_arg_textfield.clear()
        second_arg_textfield.send_keys(str(second_arg))
        sum_button.click()

        # check if sum correct
        sum_result_label = self.driver.find_element_by_accessibility_id("Answer")
        self.assertEqual(sum_result_label.text, str(first_arg + second_arg))
        print 'test_sum'


    def test_check_minus_function(self):
        first_arg = 10
        second_arg = 2

        # find elements
        first_arg_textfield = self.driver.find_element_by_accessibility_id("IntegerA")
        second_arg_textfield = self.driver.find_element_by_xpath("//UIATextField[@label='IntegerB']")
        minus_button = self.driver.find_element_by_accessibility_id("ComputeSubButton")

        # compute sum
        first_arg_textfield.clear()
        first_arg_textfield.send_keys(str(first_arg))
        second_arg_textfield.clear()
        second_arg_textfield.send_keys(str(second_arg))
        minus_button.click()

        # check if sum correct
        minus_result_label = self.driver.find_element_by_accessibility_id("SubAnswer")
        self.assertEqual(minus_result_label.text, str(first_arg - second_arg))
        print 'test_minus'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppiumIosL5)
    unittest.TextTestRunner(verbosity=2).run(suite)
