from appium import webdriver

class CustomDriver(webdriver.Remote):

    def zoom(self, element=None, percent=200, steps=50):
        touchCount = 2
        tapCount = 3
        x = 0.5
        y = 0.5
        tapOffset = {x, y}

        element.tapWithOptions({touchCount, tapCount, tapOffset});



