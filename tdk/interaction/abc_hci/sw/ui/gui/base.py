from tdk.interaction.abc_hci.base_classes import HCIBase


class View(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class Button(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    @HCIBase.register_event_trigger("click")
    def click(self):
        pass

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class CheckBox(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    @HCIBase.register_event_trigger("check")
    def check(self):
        pass

    @HCIBase.register_event_trigger("uncheck")
    def uncheck(self):
        pass

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class ComboBox(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    @HCIBase.register_event_trigger("select")
    def select(self, item):
        pass

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class Menu(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class InputField(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    @HCIBase.register_event_trigger("set_text")
    def set_text(self, text):
        pass

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class Label(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class RadioButton(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    @HCIBase.register_event_trigger("select")
    def select(self):
        pass

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class Table(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class List(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class Tree(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class TabBar(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass


class Dialog(HCIBase):
    _event_trigger_map = {}
    element_id = None
    api = None
    ext_id = None
    ext_id_type = None

    def manifest(self):
        pass

    def trigger_event(self, event_trigger_name, event_trigger_params=None):
        pass
