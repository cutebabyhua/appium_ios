#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..appium_page_objects import PageObject, page_element

class IndexPage(PageObject):

    first_arg_textfield = page_element(accessibility_id = "IntegerA")
    second_arg_textfield = page_element(xpath = "//UIATextField[@label='IntegerB']")
    minus_button = page_element(accessibility_id = "ComputeSubButton")
    minus_result = page_element(accessibility_id = "SubAnswer")

    def calculate_minus(self, a, b):
        self.first_arg_textfield = a
        self.second_arg_textfield = b
        self.minus_button.click()

