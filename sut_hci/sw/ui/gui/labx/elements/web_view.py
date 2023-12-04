from typing import List
from selenium.webdriver.remote.webelement import WebElement
from sut_hci.sw.ui.gui.labx.constants import \
    ExternalIdType

from sut_hci.sw.ui.gui.labx.factory import WebDriverFactory
from sut_hci.sw.ui.gui.reference import SutGUIElement
from tdk.interaction.abc_hci.sw.ui.gui import base


class Page(base.View):
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
        :return: Page object
        :doc-author: Gopalakrishnan
        """
        self.element_definition = element_definition
        element_id = self.element_definition.gui_element_id
        api = self.element_definition.gui_element_type
        ext_id = self.element_definition.external_identifier
        ext_id_type = self.element_definition.external_identifier_type
        self.driver = WebDriverFactory.get_current_driver()
        self.element = self.driver.find_element(
            by=self.element_definition.external_identifier_type,
            value=self.element_definition.external_identifier)
        # super().__init__(driver, element_id, api, ext_id, ext_id_type)
        _event_trigger_map = {
            "get_title": self.get_title,
            "reload": self.reload,
            "navigate_back": self.navigate_back,
            "navigate_forward": self.navigate_forward,
        }

    def get_child_by_name(self, name):
        return self.element_definition.gui_element_children[name]

    def get_title(self):
        """
        The get_title function returns the title of the current page.

        :param self: Refer to the instance of the class
        :return: The title of the current page
        :doc-author: Gopalakrishnan
        """
        return self.driver.title

    def reload(self):
        """
        The reload function refreshes the current page.

        :param self: Represent the instance of the class
        :return: The page that is currently loaded
        :doc-author: Gopalakrishnan
        """
        return self.driver.refresh()

    def navigate_back(self):
        """
        The navigate_back function navigates the browser back one page.

        :param self: Represent the instance of the class
        :return: The driver
        :doc-author: Gopalakrishnan
        """
        return self.driver.back()

    def navigate_forward(self):
        """
        The navigate_forward function navigates the browser forward one page.


        :param self: Represent the instance of the class
        :return: The current page url
        :doc-author: Gopalakrishnan
        """
        return self.driver.forward()


class WebContainer:
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
        :return: WebContainer object
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

    def get_child_by_name(self, name):
        return self.element_definition.gui_element_children[name]

    def click(self):
        self.element.click()


class WebTable(base.Table):
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
        :return: WebTable object
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
            "get_rows_count": self.get_rows_count
        }

    def manifest(self):
        super().manifest()

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        super().trigger_event(event_trigger_name, event_trigger_params)

    def get_column_names(self) -> List[str]:
        """
        The get_column_names function returns a list of column names from the
        table.

        :param self: Represent the instance of the class
        :return: A list of column names
        :doc-author: Gopalakrishnan
        """
        column_names = self.element.find_elements(
            ExternalIdType.XPATH, ".//thead//th")
        names = list(name.text for name in column_names)
        return names

    def get_row_elements(self) -> List[WebElement]:
        """
        The get_row_elements function returns a list of WebElement objects that represent the rows in the table.

        :param self: Represent the instance of the class
        :return: A list of row objects
        :doc-author: Gopalakrishnan
        """
        rows = self.element.find_elements(
            ExternalIdType.XPATH, ".//tbody//tr")
        return rows

    def get_rows_count(self) -> int:
        """
        The get_rows_count function returns the number of rows in a table.

        :param self: Represent the instance of the class
        :return: The number of rows in the table
        :doc-author: Gopalakrishnan
        """
        return len(self.get_row_elements())

    def get_cells(self) -> List[dict]:
        """
        The get_cells function returns a list of dictionaries, where each
        dictionary represents a row in the table. Each dictionary contains
        key-value pairs for each column name and cell element respectively.

        :param self: Refer to the object itself
        :return: A list of cell webelements as dictionary
        :doc-author: Gopalakrishnan
        """
        column_names: List[str] = self.get_column_names()
        rows: List[WebElement] = self.get_row_elements()
        table_data = list(dict())
        for row_index, row in enumerate(rows):
            row_data = {}
            current_row_cells = row.find_elements(
                ExternalIdType.XPATH, ".//td")
            for column_index, cell in enumerate(current_row_cells):
                column_name: str = column_names[column_index]
                row_data[column_name] = cell
            table_data.append(row_data)
        return table_data

    def get_data(self) -> List[dict]:
        """
        The get_data function returns a list of dictionaries, where each
        dictionary represents the data in one row of the table. The keys for
        each dictionary are the column names and the values are the cell
        contents.

        :param self: Refer to the object itself
        :return: A list of dictionaries
        :doc-author: Gopalakrishnan
        """
        column_names: List[str] = self.get_column_names()
        rows: List[WebElement] = self.get_row_elements()
        table_data = list(dict())
        for row_index, row in enumerate(rows):
            row_data = {}
            current_row_cells = row.find_elements(
                ExternalIdType.XPATH, ".//td")
            for column_index, cell in enumerate(current_row_cells):
                column_name: str = column_names[column_index]
                row_data[column_name] = cell.text
            table_data.append(row_data)
        return table_data

    def get_row_data_by_index(self, row_index: int) -> dict:
        """
        The get_row_data_by_index function returns a dictionary of the data
        in the row at index 'row_index' in the table. The keys are column
        names and values are cell contents.

        :param self: Represent the instance of the class
        :param row_index: int: Specify which row to return
        :return: A dictionary of the row data
        :doc-author: Gopalakrishnan
        """
        table_data = self.get_data()
        return table_data[row_index]

    def get_row_data_by_value(self, column_name: str, cell_value: str) -> \
            List[dict]:
        """
        The get_row_data_by_value function takes a column name and cell value
        as arguments. It returns a list of dictionaries, where each
        dictionary represents the data in one row of the table that matches
        the given cell value.

        :param self: Represent the instance of the class
        :param column_name: str: Specify the column name to be used for
        filtering
        :param cell_value: str: Specify the value that is to be searched for
        in the
        table
        :return: A list of dictionaries :doc-author: Gopalakrishnan
        """
        table_data = self.get_data()
        filtered_table_data = [row for row in table_data if row[
            column_name] == cell_value]
        return filtered_table_data

    def click_cell_by_value(self, column_name: str, cell_value: str):
        """
        The click_cell_by_value function takes in a column name and cell
        value as parameters. It then uses the get_cells function to retrieve
        all the table data, which is stored in a list of dictionaries. The
        next() function is used to iterate through each row (dictionary)
        until it finds one where the specified column's text matches the
        specified cell value. Once that row has been found, its corresponding
        WebElement object is clicked.

        :param self: Make the method a bound method
        :param column_name: str: Specify the column name of the table
        :param cell_value: str: Pass in the value of the cell to be clicked
        :return: A WebElement object
        :doc-author: Gopalakrishnan
        """
        table_data = self.get_cells()
        table_cell: WebElement = next((row[column_name])
                                      for row in table_data
                                      if row[column_name].text == cell_value)
        table_cell.click()


class WebMenu(base.Menu):
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
        :return: WebMenu object
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
        self.menu_items = []
        _event_trigger_map = {
            "get_menu_items": self.get_menu_items,
            "click_menu_item_by_text": self.click_menu_item_by_text,
        }

    def manifest(self):
        super().manifest()

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        super().trigger_event(event_trigger_name, event_trigger_params)

    def get_child_by_name(self, name):
        return self.element_definition.gui_element_children[name]

    def get_menu_items(self, ext_id, ext_id_type):
        """
        The get_menu_items function is a helper function that returns the
        menu items of a given menu.

        :param self: Access the class attributes and methods
        :param ext_id: Identify the element that contains the menu items
        :param ext_id_type: Find the elements in the menu
        :return: A list of elements
        :doc-author: Gopalakrishnan
        """
        self.menu_items = self.element.find_elements(
            ext_id_type, ext_id)
        return self.menu_items

    def click_menu_item_by_text(self, menu_item_text):
        """
        The click_menu_item_by_text function takes a menu_item_text argument
        and clicks the corresponding menu item. The function uses a generator
        expression to iterate through the list of menu items, checking each
        one for equality with the provided text. If there is no match,
        None is returned.

        :param self: Refer to the current object
        :param menu_item_text: Identify the menu item to be clicked
        :return: The selected menu item
        :doc-author: Gopalakrishnan
        """
        selected_menu_item: WebMenuItem = next(
            (menu_item for menu_item in self.menu_items
             if menu_item.text == menu_item_text),
            None,
        )
        selected_menu_item.click()


class WebMenuItem:
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
        :return: WebMenuItem object
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
            "click": self.click,
        }

    def click(self):
        """
        The click function is used to click on a web element.
            It takes no arguments and returns nothing.

        :param self: Represent the instance of the class
        :return: The element that was clicked
        :doc-author: Gopalakrishnan
        """
        self.element.click()
        print(f"Clicked on element: {vars(self.element_definition)}")


class WebTileGrid:
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
        :return: WebTileGrid object
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
            "get_grid_items": self.get_grid_items,
        }

    def get_grid_items(self, ext_id, ext_id_type):
        """
        The get_grid_items function is used to return a list of elements that
        are found within the grid.

        :param self: Represent the instance of the class
        :param ext_id: Specify the locator value for identifying the
        grid items
        :param ext_id_type: Specify the type of locator to be used
        :return: A list of grid items as webelements.
        :doc-author: Gopalakrishnan
        """
        return self.element.find_elements(by=ext_id_type, value=ext_id)


class WebPropertyGrid:
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
        :return: WebPropertyGrid object
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
            "get_property_grid_items": self.get_property_grid_values
        }
        self.property_grid_items = []

    def get_property_grid_values(self, ext_id, ext_id_type) -> dict:
        """
        The get_grid_items function is used to return a list of elements that
        are found within the grid.
        :param self: Represent the instance of the class
        :param ext_id: Specify the locator value for identifying the
        grid items
        :param ext_id_type: Specify the type of locator to be used
        :return: A list of grid items as webelements.
        :doc-author: Gopalakrishnan
        """
        self.property_grid_items: List[WebElement] = \
            self.element.find_elements(
                ext_id_type, ext_id)
        property_grid_values = dict()
        for property_grid_item in self.property_grid_items:
            property_name = property_grid_item.find_element(
                ExternalIdType.XPATH, ".//span["
                                      "@data-cy='PropertyCell-Name']").text
            property_value = property_grid_item.find_element(
                ExternalIdType.XPATH, ".//span["
                                      "@data-cy='PropertyCell-Value']").text
            property_grid_values[property_name] = property_value
        return property_grid_values

    def get_property_value(self, property_name) -> str:
        """
        The get_property_value function returns the value of a property in
        the Property Grid.

        :param self: Represent the instance of the class
        :param property_name: Get the value of a specific property
        :return: The value of a property
        :doc-author: Gopalakrishnan
        """
        property_grid_values = self.get_property_grid_values(
            ".//div[contains(@class,'property-cell')]", ExternalIdType.XPATH)
        return property_grid_values[property_name]
