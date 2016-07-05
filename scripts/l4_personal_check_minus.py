# -*- coding:utf-8 -*-
import os
import unittest
import sys

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

SCREENSHOT_NAME = "check_sum_error.png"

class TestAppiumIosL4(unittest.TestCase):

    # 脚本初始化步骤,对应"前置步骤",每次执行test函数时均会先执行.
    def setUp(self):
        # open TestApp.app on simulator iPhone 5s (9.3)
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'

        # simulator
        desired_caps['deviceName'] = 'iPhone 5s'
        desired_caps['app'] = PATH(
            '../app/TestApp/build/Debug-iphonesimulator/TestApp.app'
        )



        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # clear screenshot
        if os.path.exists(SCREENSHOT_NAME):
            os.remove(SCREENSHOT_NAME)

    # 脚本收尾步骤,对应"恢复原状",每次执行test函数后均会执行.
    def tearDown(self):

        # check if need to take screenshot
        if sys.exc_info()[0]:  # Returns the info of exception being handled
            # take screenshot
            self.driver.save_screenshot(SCREENSHOT_NAME)

        # end the session
        self.driver.quit()

    # 具体测试内容,函数名必须以test_开头
    def test_check_sum_function(self):
        first_arg = 10
        second_arg = 2

        # find elements
        first_arg_textfield = self.driver.find_element_by_accessibility_id("IntegerA")
        second_arg_textfield = self.driver.find_element_by_xpath("//UIATextField[@label='IntegerB']")
        sum_button = self.driver.find_element_by_accessibility_id("ComputeSumButton")
        sub_button = self.driver.find_element_by_accessibility_id("ComputeSubButton")

        # compute sum
        first_arg_textfield.send_keys(str(first_arg))
        second_arg_textfield.send_keys(str(second_arg))
        # sum_button.click()
        sub_button.click()

        # check if sum correct
        # sum_result_label = self.driver.find_element_by_accessibility_id("Answer")
        sum_result_label = self.driver.find_element_by_accessibility_id("SubAnswer")
        self.assertEqual(sum_result_label.text, str(first_arg - second_arg))



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppiumIosL4)
    unittest.TextTestRunner(verbosity=2).run(suite)
