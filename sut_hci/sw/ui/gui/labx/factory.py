from typing import Union

from selenium.webdriver.chromium.webdriver import ChromiumDriver as ChromeDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from seleniumbase import get_driver


class WebDriverFactory:
    driver = None
    supported_browsers = ["chrome", "firefox", "edge"]

    @classmethod
    def initialize(cls, browser_name: str = "edge",
                   headless_mode_enabled: bool = False):
        """
        The initialize function is a class method that initializes the driver
        instance of the given browser. It also sets an implicit wait time and
        maximizes the window. The initialize function is called by all test
        classes to get a driver instance for their tests.

        :param cls: Specify the class that is being initialized
        :param browser_name: str: Specify the browser that will be used to
        run the tests
        :param headless_mode_enabled: bool: Indicate whether the browser
        should be launched in headless mode or not
        :return: The driver object
        :doc-author: Gopalakrishnan
        """
        if not cls.driver:
            if browser_name in cls.supported_browsers:
                # Launch the given browser from the list of supported browsers.
                cls.driver = get_driver(browser_name,
                                        headless_mode_enabled)
            else:
                # Throw exception when the given browser is not supported.
                raise Exception(f"The given browser '{browser_name}' is not "
                                f"supported")
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def get_current_driver(cls) -> Union[
            ChromeDriver, FirefoxDriver, EdgeDriver]:
        """
        The get_current_driver function returns the current driver instance.
        :param cls: Refer to the class itself
        :return: The current driver
        :doc-author: Gopalakrishnan
        """
        return cls.driver
