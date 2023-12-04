import time

from sut_hci.sw.ui.gui.labx.config import AppConfig
from sut_hci.sw.ui.gui.labx.constants import ExternalIdType
from sut_hci.sw.ui.gui.labx.elements.web_view import WebContainer, WebMenu, \
    WebMenuItem, WebTable, WebPropertyGrid, Page
from sut_hci.sw.ui.gui.labx.elements.web_input import WebTextBox, WebButton, \
    WebCheckBoxDropdown
from sut_hci.sw.ui.gui.labx.elements.web_text import WebLabel
from sut_hci.sw.ui.gui.labx.factory import WebDriverFactory
from sut_hci.sw.ui.gui.reference import SutGUIElement


def test_lxc_login_correct_password():
    driver = WebDriverFactory.initialize()
    try:
        # Launch browser and navigate to labx application.
        driver.get(AppConfig.LABX_URL)

        # Login page elements.
        login_page_username_element_definition = SutGUIElement(
            gui_element_id=1, gui_element_name="login_page_username",
            gui_element_type=Page, gui_element_version="1.0",
            external_identifier="LoginName",
            external_identifier_type=ExternalIdType.ID)
        login_page_username_textbox = WebTextBox(
            login_page_username_element_definition
        )
        login_page_password_element_definition = SutGUIElement(
            gui_element_id=1, gui_element_name="login_page_password",
            gui_element_type=Page, gui_element_version="1.0",
            external_identifier="Password",
            external_identifier_type=ExternalIdType.ID)
        login_page_password_textbox = WebTextBox(
            login_page_password_element_definition
        )
        login_page_login_button_element_definition = SutGUIElement(
            gui_element_id=1, gui_element_name="login_page_login_button",
            gui_element_type=Page, gui_element_version="1.0",
            external_identifier="btn-signin",
            external_identifier_type=ExternalIdType.ID)
        login_page_login_button = WebButton(
            login_page_login_button_element_definition
        )
        login_page_element_definition = SutGUIElement(
            gui_element_id=1, gui_element_name="login_page",
            gui_element_type=Page, gui_element_version="1.0",
            external_identifier="//div[@class='container-login-custom']",
            external_identifier_type=ExternalIdType.XPATH,
            gui_element_children={
                "textbox_username": login_page_username_textbox,
                "textbox_password": login_page_password_textbox,
                "button_login": login_page_login_button
            }
        )
        login_page = Page(login_page_element_definition)
        username = login_page.get_child_by_name("textbox_username")
        password = login_page.get_child_by_name("textbox_password")
        login = login_page.get_child_by_name("button_login")

        # Login to labx application.
        username.set_text("Default")
        password.set_text("Default!1234")
        login.click()

        # Main page elements.
        # Sidebar.
        menu_item_resources_element_definition = SutGUIElement(
            gui_element_id=1, gui_element_name="menu_item_resources",
            gui_element_type=WebMenuItem, gui_element_version="1.0",
            external_identifier="//div["
                                "@data-cy='mtSideBar-sidebarListItemTitle' "
                                "and contains(text(),'Resources')]",
            external_identifier_type=ExternalIdType.XPATH)

        menu_item_resources = WebMenuItem(
            menu_item_resources_element_definition
        )

        menu_element_definition = SutGUIElement(
            gui_element_id=1, gui_element_name="menu",
            gui_element_type=WebMenu, gui_element_version="1.0",
            external_identifier="//nav[@data-cy='mtSideBar-navigationDrawer']",
            external_identifier_type=ExternalIdType.XPATH,
            gui_element_children={
                "menu_item_resources": menu_item_resources
            })

        menu = WebMenu(menu_element_definition)

        # Analysis grid page elements.
        analysis_grid_page_element_definition = SutGUIElement(
            gui_element_id=1, gui_element_name="analysis_grid_page",
            gui_element_type=Page, gui_element_version="1.0",
            external_identifier="//div[@id='app']",
            external_identifier_type=ExternalIdType.XPATH,
            gui_element_children={
                "menu": menu
            }
        )
        analysis_grid_page = Page(analysis_grid_page_element_definition)

        # Click on resources menu item in sidebar.
        menu_item_resources = analysis_grid_page.get_child_by_name(
            "menu").get_child_by_name(
            "menu_item_resources")
        menu_item_resources.click()

        # Instruments and resources grid page elements.
        grid_tile_instruments_and_resources_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="grid_tile_instrument_and_resources",
            gui_element_type=WebContainer, gui_element_version="1.0",
            external_identifier="//div["
                                "@data-cy='InstrumentsResourcesApp-tile']",
            external_identifier_type=ExternalIdType.XPATH)

        grid_tile_instruments_and_resources = WebContainer(
            grid_tile_instruments_and_resources_element_definition
        )

        grid_instruments_and_resources_element_definition = SutGUIElement(
            gui_element_id=1, gui_element_name="grid_instrument_and_resources",
            gui_element_type=WebContainer, gui_element_version="1.0",
            external_identifier="//nav[@data-cy='mtSideBar-navigationDrawer"
                                "']//div[contains(text(),'Resources')]",
            external_identifier_type=ExternalIdType.XPATH,
            gui_element_children={
                "menu": menu,
                "grid_tile_instruments_and_resources":
                    grid_tile_instruments_and_resources
            }
        )

        grid_instruments_and_resources = WebContainer(
            grid_instruments_and_resources_element_definition
        )

        instruments_and_resources_grid_page_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="instruments_and_resources_grid_page",
            gui_element_type=Page, gui_element_version="1.0",
            external_identifier="//main[@data-cy='MainApp-main']",
            external_identifier_type=ExternalIdType.XPATH,
            gui_element_children={
                "menu": menu,
                "grid_instruments_and_resources":
                    grid_instruments_and_resources
            }
        )
        instruments_and_resources_grid_page = Page(
            instruments_and_resources_grid_page_element_definition
        )

        # Click on instruments and resources grid tile.
        instruments_and_resources_grid_tile = grid_instruments_and_resources. \
            get_child_by_name("grid_tile_instruments_and_resources")
        instruments_and_resources_grid_tile.click()

        # Analysis grid page elements.
        menu_item_resources_element_definition = SutGUIElement(
            gui_element_id=1, gui_element_name="menu_item_resources",
            gui_element_type=WebMenuItem, gui_element_version="1.0",
            external_identifier="//div["
                                "@data-cy='mtSideBar-sidebarListItemTitle' "
                                "and contains(text(),'Resources')]",
            external_identifier_type=ExternalIdType.XPATH)

        menu_item_resources = WebMenuItem(
            menu_item_resources_element_definition
        )
        menu_item_instruments_element_definition = SutGUIElement(
            gui_element_id=1, gui_element_name="menu_item_instruments",
            gui_element_type=WebMenuItem, gui_element_version="1.0",
            external_identifier="//div["
                                "@data-cy='mtSideBar-sidebarListItemTitle' "
                                "and contains(text(),'Instruments')]",
            external_identifier_type=ExternalIdType.XPATH)

        menu_item_instruments = WebMenuItem(
            menu_item_instruments_element_definition
        )

        menu_element_definition = SutGUIElement(
            gui_element_id=1, gui_element_name="menu",
            gui_element_type=WebMenu, gui_element_version="1.0",
            external_identifier="//nav[@data-cy='mtSideBar-navigationDrawer']",
            external_identifier_type=ExternalIdType.XPATH,
            gui_element_children={
                "menu_item_resources": menu_item_resources,
                "menu_item_instruments": menu_item_instruments
            })

        menu = WebMenu(menu_element_definition)

        instruments_and_resources_page_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="analysis_grid_page",
            gui_element_type=Page, gui_element_version="1.0",
            external_identifier="//div[@id='app']",
            external_identifier_type=ExternalIdType.XPATH,
            gui_element_children={
                "menu": menu
            }
        )
        instruments_and_resources_page = Page(
            instruments_and_resources_page_element_definition
        )

        # Click on instruments menu item.
        menu_item_instruments = menu. \
            get_child_by_name("menu_item_instruments")
        menu_item_instruments.click()
        print("Clicked on instruments menu item")

        # Click on resources menu item.
        menu_item_resources = menu. \
            get_child_by_name("menu_item_resources")
        menu_item_resources.click()
        print("Clicked on resources menu item")
        time.sleep(1)
        refresh_button_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="refresh_button",
            gui_element_type=WebButton, gui_element_version="1.0",
            external_identifier=".//div[@data-cy='ResourceList-refreshList"
                                "-button']",
            external_identifier_type=ExternalIdType.XPATH
        )

        refresh_button = WebButton(
            refresh_button_element_definition
        )

        last_refresh_time_label_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="refresh_button",
            gui_element_type=WebLabel, gui_element_version="1.0",
            external_identifier=
            ".//span[@data-cy='MtDataTableActionBarLastRefreshTimeLabelDate']",
            external_identifier_type=ExternalIdType.XPATH
        )

        last_refresh_time_label = WebLabel(
            last_refresh_time_label_element_definition
        )

        hide_filters_button_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="hide_filters_button",
            gui_element_type=WebButton, gui_element_version="1.0",
            external_identifier=
            ".//button[@data-cy='MtDataTableActionBarButtonToggleFilter']",
            external_identifier_type=ExternalIdType.XPATH
        )

        hide_filters_button = WebButton(
            hide_filters_button_element_definition
        )

        name_filter_textbox_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="name_filter_textbox",
            gui_element_type=WebTextBox, gui_element_version="1.0",
            external_identifier=
            ".//input[@data-cy='MtDataTableFilterName']",
            external_identifier_type=ExternalIdType.XPATH
        )

        name_filter_textbox = WebTextBox(
            name_filter_textbox_element_definition
        )

        id_filter_textbox_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="id_filter_textbox",
            gui_element_type=WebTextBox, gui_element_version="1.0",
            external_identifier=
            ".//input[@data-cy='MtDataTableFilterUserDefinedId']",
            external_identifier_type=ExternalIdType.XPATH
        )

        id_filter_textbox = WebTextBox(
            id_filter_textbox_element_definition
        )

        class_filter_checkbox_dropdown_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="class_filter_checkbox_dropdown",
            gui_element_type=WebCheckBoxDropdown, gui_element_version="1.0",
            external_identifier=
            ".//label[text()='Class']//ancestor::div[@aria-haspopup='listbox']",
            external_identifier_type=ExternalIdType.XPATH
        )

        class_filter_checkbox_dropdown = WebCheckBoxDropdown(
            class_filter_checkbox_dropdown_element_definition
        )

        apply_filters_button_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="apply_filters_button",
            gui_element_type=WebButton, gui_element_version="1.0",
            external_identifier=
            ".//button[@data-cy='MtDataTableFilterButtonApply']",
            external_identifier_type=ExternalIdType.XPATH
        )

        apply_filters_button = WebButton(
            apply_filters_button_element_definition
        )

        list_page_table_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="list_page_table",
            gui_element_type=WebTable, gui_element_version="1.0",
            external_identifier=
            "//div[@data-cy='MtDataTableOverlayWrapper']//table",
            external_identifier_type=ExternalIdType.XPATH
        )

        list_page_table = WebTable(
            list_page_table_element_definition
        )

        resources_list_page_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="resources_list_page",
            gui_element_type=Page, gui_element_version="1.0",
            external_identifier="//div[@id='app']",
            external_identifier_type=ExternalIdType.XPATH,
            gui_element_children={
                "menu": menu,
                "refresh_button": refresh_button,
                "last_refresh_time_label": last_refresh_time_label,
                "hide_filters_button": hide_filters_button,
                "class_filter_checkbox_dropdown":
                    class_filter_checkbox_dropdown,
                "name_filter_textbox": name_filter_textbox,
                "id_filter_textbox": id_filter_textbox,
                "apply_filters_button": apply_filters_button,
                "list_page_table": list_page_table

            }
        )
        resources_list_page = Page(
            resources_list_page_element_definition
        )
        refresh_button = resources_list_page. \
            get_child_by_name("refresh_button")
        refresh_button.click()
        print("Clicked on refresh button")
        refresh_button = resources_list_page. \
            get_child_by_name("last_refresh_time_label")
        print(refresh_button.get_text())
        class_filter_checkbox_dropdown = resources_list_page. \
            get_child_by_name("class_filter_checkbox_dropdown")
        class_filter_checkbox_dropdown.select_options_by_text(["Blank value",
                                                               "Stirrer"])
        name_filter_textbox = resources_list_page. \
            get_child_by_name("name_filter_textbox")
        name_filter_textbox.set_text("Stirrer 1")
        id_filter_textbox = resources_list_page. \
            get_child_by_name("id_filter_textbox")
        id_filter_textbox.set_text("")
        apply_filters_button = resources_list_page. \
            get_child_by_name("apply_filters_button")
        apply_filters_button.click()
        hide_filters_button = resources_list_page. \
            get_child_by_name("hide_filters_button")
        hide_filters_button.click()

        list_page_table = resources_list_page. \
            get_child_by_name("list_page_table")
        print(list_page_table.get_data())
        list_page_table.click_cell_by_value("Name", "Stirrer 1")

        back_button_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="back_button",
            gui_element_type=WebButton, gui_element_version="1.0",
            external_identifier=
            ".//div[@data-cy='ResourceDetailsView-cancel-button']",
            external_identifier_type=ExternalIdType.XPATH
        )

        back_button = WebButton(
            back_button_element_definition
        )

        general_property_grid_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="general_property_grid",
            gui_element_type=WebPropertyGrid, gui_element_version="1.0",
            external_identifier=
            ".//h1[@id='general']//following::div[1]",
            external_identifier_type=ExternalIdType.XPATH
        )

        general_property_grid = WebPropertyGrid(
            general_property_grid_element_definition
        )

        master_table_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="master_table",
            gui_element_type=WebTable, gui_element_version="1.0",
            external_identifier=
            ".//h1[@id='masterData']//following::table[1]",
            external_identifier_type=ExternalIdType.XPATH
        )

        master_table = WebTable(
            master_table_element_definition
        )

        instruments_table_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="instruments_table",
            gui_element_type=WebTable, gui_element_version="1.0",
            external_identifier=
            ".//h1[@id='instruments']//following::table[1]",
            external_identifier_type=ExternalIdType.XPATH
        )

        instruments_table = WebTable(
            instruments_table_element_definition
        )

        resources_details_page_element_definition = SutGUIElement(
            gui_element_id=1,
            gui_element_name="resources_details_page",
            gui_element_type=Page, gui_element_version="1.0",
            external_identifier="//div[@id='app']",
            external_identifier_type=ExternalIdType.XPATH,
            gui_element_children={
                "menu": menu,
                "back_button": back_button,
                "general_property_grid": general_property_grid,
                "master_table": master_table,
                "instruments_table": instruments_table,

            }
        )
        resources_details_page = Page(
            resources_details_page_element_definition
        )

        general_property_grid = resources_details_page. \
            get_child_by_name("general_property_grid")
        print(general_property_grid.get_property_value("Class"))

        master_table = resources_details_page. \
            get_child_by_name("master_table")
        print(master_table.get_data())

        instruments_table = resources_details_page. \
            get_child_by_name("instruments_table")
        print(instruments_table.get_data())
    except Exception as e:
        print(e)
    finally:
        driver.quit()


if __name__ == '__main__':
    test_lxc_login_correct_password()
