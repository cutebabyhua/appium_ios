# -*- coding:utf-8 -*-
import os
import unittest
import sys

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
# from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestL6(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['deviceName'] = 'iPhone 5s'
        desired_caps['app'] = PATH(
            '/Users/chenjinhua/git/appium_ios/app/AppForUITest/appForUITest/build/Debug-iphonesimulator/appForUITest.app'
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print 'setUp'

    def tearDown(self):
        if sys.exc_info()[0]:  # Returns the info of exception being handled
            self.driver.save_screenshot(self.id().split(".")[-1]+".png")
        self.driver.quit()
        print 'tearDown'

    def test_gesture_unlock(self):
        # 查找元素 操作  校验
        self.driver.find_element_by_xpath("//UIAButton[@label='Gesture']").click()
        self.driver.find_element_by_accessibility_id("Gesture Locker (TouchAction)").click()

        btn3 = self.driver.find_element_by_accessibility_id("Button3")
        btn6 = self.driver.find_element_by_accessibility_id("Button6")
        btn5 = self.driver.find_element_by_accessibility_id("Button5")
        btn7 = self.driver.find_element_by_accessibility_id("Button7")
        btn1 = self.driver.find_element_by_accessibility_id("Button1")

        action1 = TouchAction(self.driver)
        action1.press(btn3).wait(100).move_to(btn6).wait(100).move_to(btn5).wait(100).move_to(btn7).wait(100).move_to(btn1).wait(100).release().perform()

        action2 = TouchAction(self.driver)
        action2.press(btn3).wait(100).move_to(btn6).wait(100).move_to(btn5).wait(100).move_to(btn7).wait(100).move_to(btn1).wait(100).release().perform()

        hintString = self.driver.find_element_by_accessibility_id("password has been setup!")
        self.assertEqual(hintString.text,"password has been setup!")
        print "手势校验通过"

        action3 = TouchAction(self.driver)
        action3.press(btn3).wait(100).move_to(btn6).wait(100).move_to(btn5).wait(100).move_to(btn7).wait(100).move_to(btn1).wait(100).release().perform()
        print "手势解锁完成"



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestL6)
    unittest.TextTestRunner(verbosity=2).run(suite)
