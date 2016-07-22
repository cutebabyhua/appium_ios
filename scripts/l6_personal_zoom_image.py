# -*- coding:utf-8 -*-
import os
import unittest
import sys

# from custom_driver.custom_driver import CustomDriver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
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

    def test_zoom_image(self):
        # 查找元素 操作  校验
        self.driver.find_element_by_xpath("//UIAButton[@label='Gesture']").click()
        self.driver.find_element_by_accessibility_id("Image (Zoom and Pinch)").click()

        image = self.driver.find_element_by_accessibility_id("imageScrollView")
        location = image.location

        # 获取image的坐标,为(20,90)
        print location
        x = location["x"]
        y = location["y"]
        print x
        print y

        # 获取image的宽和高,分别为300,300
        size = image.size
        print size

        a1 = TouchAction()
        a1.press(30, 100).move_to(30, 150).release()
        a2 = TouchAction()
        a2.press(30, 100).move_to(30, 50).release()
        MultiAction(self.driver).add(a1, a2).perform()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestL6)
    unittest.TextTestRunner(verbosity=2).run(suite)
