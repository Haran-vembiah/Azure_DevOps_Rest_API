from sut_hci.sw.ui.gui.labx.factory import WebDriverFactory
from sut_hci.sw.ui.gui.reference import SutGUIElement
from tdk.interaction.abc_hci.sw.ui.gui import base


class WebLabel(base.Label):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def __init__(self, element_definition: SutGUIElement):
        _event_trigger_map = {}
        element_id = None
        api = None
        ext_id = None
        ext_id_type = None

        """
        The __init__ function is called when the class is instantiated.
        It sets up the instance of the class, and makes sure that it has all the
        attributes necessary for proper functioning.

        :param self: Represent the instance of the class
        :param element_definition: SutGUIElement: Definition of the element
        :return: WebGrid object
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
            "get_text": self.get_text
        }

    def manifest(self):
        super().manifest()

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        super().trigger_event(event_trigger_name, event_trigger_params)

    def get_text(self) -> str:
        """
        The get_text function returns the text of an element.
        :param self: Access the class attributes
        :return: The text of the element
        :doc-author: Gopalakrishnan
        """
        return self.element.text

    def click(self):
        """
        The click function is used to click on a web element.
            It takes no arguments and returns nothing.
        :param self: Represent the instance of the class
        :return: Nothing
        :doc-author: Gopalakrishnan
        """
        self.element.click()
        print(f"Clicked on element: {vars(self.element_definition)}")


class WebLink:
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
        :return: WebGrid object
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
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass

    def click(self):
        """
        The click function is used to click on a web element.
            It takes no arguments and returns nothing.
        :param self: Represent the instance of the class
        :return: Nothing
        :doc-author: Gopalakrishnan
        """
        self.element.click()
        print(f"Clicked on element: {vars(self.element_definition)}")
