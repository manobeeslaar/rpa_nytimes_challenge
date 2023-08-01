# initial bot
from RPA.Browser.Selenium import Selenium

# browser class


class BrowserBot:

    def __init__(self) -> None:
        self.browser = Selenium()

    def open_available_browser(self, url, headless=False):
        self.browser.open_available_browser(url, headless=headless)
        return self.browser

    def wait_until_page_contains_element(self, xpath):
        self.browser.wait_until_page_contains_element(xpath)
        return self.browser

    def close_browser(self):
        self.browser.close_browser()
        return self.browser

    def click_button(self, xpath):
        self.browser.click_button(xpath)
        return self.browser

    def input_text(self, xpath, text):
        self.browser.input_text(xpath, text)
        return self.browser

    def get_text(self, xpath):
        return self.browser.get_text(xpath)

    def get_source(self):
        return self.browser.get_source()

    def get_title(self):
        return self.browser.get_title()

    def get_cookies(self):
        return self.browser.get_cookies()

    def press_keys(self, xpath, keys):
        self.browser.press_keys(xpath, keys)
        return self.browser

    def get_value(self, xpath):
        return self.browser.get_value(xpath)

    def get_webelements(self, xpath):
        return self.browser.get_webelements(xpath)

    def click_element(self, xpath):
        self.browser.click_element(xpath)
        return self.browser

    def is_element_visible(self, xpath):
        return self.browser.is_element_visible(xpath)

    def get_element_attribute(self, xpath, attribute):
        return self.browser.get_element_attribute(xpath, attribute)
