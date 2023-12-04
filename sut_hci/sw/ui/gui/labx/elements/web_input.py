import time
from typing import List

from selenium.webdriver.remote.webelement import WebElement
from sut_hci.sw.ui.gui.labx.constants import \
    ExternalIdType
from sut_hci.sw.ui.gui.labx.factory import WebDriverFactory
from sut_hci.sw.ui.gui.reference import SutGUIElement
from tdk.interaction.abc_hci.sw.ui.gui import base


class WebButton(base.Button):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def __init__(self, element_definition: SutGUIElement):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the instance of the class, and makes sure that it has all the
        attributes necessary for proper functioning.

        :param self: Represent the instance of the class
        :param element_definition: SutGUIElement: Definition of the element
        :return: WebButton object
        :doc-author: Gopalakrishnan
        """
        self.element_definition = element_definition
        element_id = self.element_definition.gui_element_id
        api = self.element_definition.gui_element_type
        ext_id = self.element_definition.external_identifier
        ext_id_type = self.element_definition.external_identifier_type
        self.driver = WebDriverFactory.get_current_driver()
        self.element = self.driver.find_element(ext_id_type, ext_id)
        # super().__init__(driver, element_id, api, ext_id, ext_id_type)
        _event_trigger_map = {
            "click": self.click
        }

    def manifest(self):
        super().manifest()

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        super().trigger_event(event_trigger_name, event_trigger_params)

    def click(self):
        """
        The click function is used to click on a web element. It takes no
        arguments and returns nothing.

        :param self: Represent the instance of the class
        :return: Nothing
        :doc-author: Gopalakrishnan
        """
        self.element.click()
        print(f"Clicked on element: {vars(self.element_definition)}")


class WebTextBox(base.InputField):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def __init__(self, element_definition: SutGUIElement):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the instance of the class, and makes sure that it has all the
        attributes necessary for proper functioning.

        :param self: Represent the instance of the class
        :param element_definition: SutGUIElement: Definition of the element
        :return: WebTextBox object
        :doc-author: Gopalakrishnan
        """
        self.element_definition = element_definition
        element_id = self.element_definition.gui_element_id
        api = self.element_definition.gui_element_type
        ext_id = self.element_definition.external_identifier
        ext_id_type = self.element_definition.external_identifier_type
        self.driver = WebDriverFactory.get_current_driver()
        self.element = self.driver.find_element(ext_id_type, ext_id)
        # super().__init__(driver, element_id, api, ext_id, ext_id_type)
        _event_trigger_map = {
            "get_text": self.get_text,
            "set_text": self.set_text
        }

    def manifest(self):
        super().manifest()

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        super().trigger_event(event_trigger_name, event_trigger_params)

    def get_text(self) -> str:
        """
        The get_text function returns the text of an element.

        :param self: Refer to the object itself
        :return: The text of the element
        :doc-author: Gopalakrishnan
        """
        return self.element.text

    def set_text(self, text: str):
        """
        The set_text function is used to set the text of a given element.
            Args:
                text (str): The text that will be entered into the element.

        :param self: Represent the instance of the class
        :param text: str: Set the text value of the element
        :return: The text that the user has inputted
        :doc-author: Gopalakrishnan
        """
        self.element.click()
        self.element.send_keys(text)
        print(f"Entered text '{text}' on element:"
              f" {vars(self.element_definition)}")
        

class WebCheckBox(base.CheckBox):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def __init__(self, element_definition: SutGUIElement):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the instance of the class, and makes sure that it has all the
        attributes necessary for proper functioning.

        :param self: Represent the instance of the class
        :param element_definition: SutGUIElement: Definition of the element
        :return: WebCheckBox object
        :doc-author: Gopalakrishnan
        """
        self.element_definition = element_definition
        element_id = self.element_definition.gui_element_id
        api = self.element_definition.gui_element_type
        ext_id = self.element_definition.external_identifier
        ext_id_type = self.element_definition.external_identifier_type
        self.driver = WebDriverFactory.get_current_driver()
        self.element = self.driver.find_element(ext_id_type, ext_id)
        # super().__init__(driver, element_id, api, ext_id, ext_id_type)
        _event_trigger_map = {
            "check": self.check,
            "uncheck": self.uncheck,
            "is_checked": self.is_checked,
        }

    def manifest(self):
        super().manifest()

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        super().trigger_event(event_trigger_name, event_trigger_params)

    def check(self) -> bool:
        """
        The check function is used to check a checkbox.
        :param self: Represent the instance of the class
        :return: True if the checkbox is checked, False otherwise.
        :doc-author: Gopalakrishnan
        """
        if not self.is_checked():
            self.element.click()
            print(f"Checked the checkbox: {vars(self.element_definition)}")
        return self.is_checked()

    def uncheck(self) -> bool:
        """
        The uncheck function is used to uncheck a checkbox.
        :param self: Represent the instance of the class
        :return: True if the checkbox is unchecked, False otherwise.
        :doc-author: Gopalakrishnan
        """
        if self.is_checked():
            self.element.click()
            print(f"Unchecked the checkbox: {vars(self.element_definition)}")
        return not self.is_checked()

    def is_checked(self) -> bool:
        """
        The is_checked function checks to see if the checkbox is checked.
            If it is, then it returns True. Otherwise, it returns False.
        :param self: Represent the instance of the class
        :return: True if the checkbox is checked, False otherwise.
        :doc-author: Gopalakrishnan
        """
        checkbox_icon = self.element.find_element(
            ExternalIdType.XPATH, "//i[contains(@class, 'checkbox']")
        is_checked = False
        if "checkbox-marked" in checkbox_icon.get_attribute("class"):
            is_checked = True
        return is_checked


class WebCheckBoxDropdown(base.ComboBox):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def __init__(self, element_definition: SutGUIElement):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the instance of the class, and makes sure that it has all the
        attributes necessary for proper functioning.

        :param self: Represent the instance of the class
        :param element_definition: SutGUIElement: Definition of the element
        :return: WebCheckBoxDropdown object
        :doc-author: Gopalakrishnan
        """
        self.element_definition = element_definition
        element_id = self.element_definition.gui_element_id
        api = self.element_definition.gui_element_type
        ext_id = self.element_definition.external_identifier
        ext_id_type = self.element_definition.external_identifier_type
        self.driver = WebDriverFactory.get_current_driver()
        self.element = self.driver.find_element(ext_id_type, ext_id)
        # super().__init__(driver, element_id, api, ext_id, ext_id_type)
        self.options = []
        _event_trigger_map = {}

    def manifest(self):
        super().manifest()

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        super().trigger_event(event_trigger_name, event_trigger_params)

    def select_options_by_text(self, options_label: List[str]):
        """
        The select_options_by_text function takes a list of strings as an
        argument. It then clicks on the select element, and gets all the
        options. Then it loops through each string in the list and selects
        that option by clicking on its checkbox.

        :param self: Represent the instance of the object itself
        :param options_label: List[str]: Specify the type of data that is
        expected to be passed into the function
        :return: A list of the selected options
        :doc-author: Gopalakrishnan
        """
        self.element.click()
        print(f"Clicked on checkbox dropdown element:"
              f" {vars(self.element_definition)}")
        time.sleep(0.5)
        options = self.get_options()
        for option_label in options_label:
            option_checkbox = options.get(option_label)
            option_checkbox.click()
            print(f"Selecting the checkbox dropdown option: {option_label}")

    def get_options(self):
        """
        The get_options function returns a dictionary of WebCheckBox objects.
        The keys are the labels for each option, and the values are the checkboxes themselves.


        :param self: Refer to the current instance of a class
        :return: A dictionary of WebCheckbox objects
        :doc-author: Gopalakrishnan
        """
        options_dict: {str: WebElement} = {}
        self.options: List[WebElement] = self.driver.find_elements(
            ExternalIdType.XPATH,
            ".//div[@role='listbox']//div[@role='option']")
        for option in self.options:
            option_label = option.find_element(
                ExternalIdType.XPATH,
                ".//div[contains(@class, 'title')]"
            ).text
            option_checkbox = option.find_element(
                ExternalIdType.XPATH,
                ".//div[contains(@class, 'checkbox')]"
            )
            options_dict[option_label] = option_checkbox
        print(f"Checkbox dropdown options: {options_dict}")
        return options_dict
