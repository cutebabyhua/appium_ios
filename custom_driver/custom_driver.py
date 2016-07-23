from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

class CustomDriver(webdriver.Remote):

    def zoom(self, element=None, percent=200, steps=50):

        location = element.location
        size = element.size
        x = location["x"]+size["width"]/2
        y = location["y"]+size["height"]/2


        a1 = TouchAction()
        a1.press(x, y).move_to(x, y-30).release()
        a2 = TouchAction()
        a2.press(x, y).move_to(x, y+30).release()
        MultiAction(self).add(a1, a2).perform()

    def pinch(self, element=None, percent=200, steps=50):

        location = element.location
        size = element.size
        x = location["x"]+size["width"]/2
        y = location["y"]+size["height"]/2

        a1 = TouchAction()
        a1.press(x, y-30).move_to(x, y).release()
        a2 = TouchAction()
        a2.press(x, y+30).move_to(x, y).release()
        MultiAction(self).add(a1, a2).perform()