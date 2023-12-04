from typing import Optional, Dict, List

from tdk.interaction.abc_hci.base_classes import HCIBase


class SutGUIElement:

    def __init__(self, gui_element_id: int, gui_element_version: str,
                 gui_element_name: str,
                 gui_element_type: object, external_identifier: str,
                 external_identifier_type: str,
                 gui_element_attributes: Optional[object] = None,
                 container_element_version: Optional[str] = None,
                 gui_element_children: Optional[Dict[str, object]] = None):
        self.gui_element_id = gui_element_id
        self.gui_element_version = gui_element_version
        self.gui_element_name = gui_element_name
        self.gui_element_type = gui_element_type
        self.external_identifier = external_identifier
        self.external_identifier_type = external_identifier_type
        self.gui_element_attributes = gui_element_attributes
        self.container_element_version = container_element_version
        self.gui_element_children = gui_element_children
