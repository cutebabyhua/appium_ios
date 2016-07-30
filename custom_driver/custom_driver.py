from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

class CustomDriver(webdriver.Remote):

    def zoom(self, element=None, percent=200, steps=50):
        # calculate startX, startY, endX, endY our self
        location = element.location
        size = element.size

        startX = location["x"] + size["width"] / 2
        startY = location["x"] + size["height"] / 2

        # calculate end location using percentage
        endX = startX + size["width"] / 2 * (percent - 100) / 100.0
        endY = startY + size["height"] / 2 * (percent -100) / 100.0

        opts = {
            'startX': startX,
            'startY': startY,
            'endX': endX,
            'endY': endY,
            'duration': steps / 10
        }
        self.execute_script('mobile: pinchOpen', opts)
        return self