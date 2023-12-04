from abc import ABCMeta, abstractmethod, ABC
from typing import Any


class HCIMeta(ABCMeta):
    """
    This metaclass is responsible for enforcing the creation of mandatory attributes and methods in HCI classes.

    Mandatory attributes and methods are the ones that ensure the HCI classes remain
    compatible with the test automation framework and its underlying architecture and data model.
    The use of a MetaClass is necessary because if a method is overridden in a subclass, without considering the
    attributes they access, once the class is instantiated accessed by other parts of the framework, it may fail.
    This is similar to defining constraints in a database to ensure data integrity.

    .. note::
    If you modify this metaclass, make sure that you only add code that is relevant to all HCI classes, and implements
    or enforces behavior that is deeply ingrained in the test automation framework, not only in the way HCI
    elements are structured or used.

    .. seealso::
        * :external-link:
    """

    def __new__(mcs, name, bases, mcs_dict):
        # Mandatory attributes and (optionally) their types. In most cases it is better to just use Any as the type,
        # otherwise it can get overly restrictive with no real benefit.
        mandatory_class_attributes = {}

        # First we need to make sure that all mandatory attributes are defined in the subclass of the HCI base class.
        # But NOT in the HCI base class itself, because that may cause an infinite recursion. -> `if bases:`
        if bases:
            for attr_name, attr_type in mandatory_class_attributes.items():
                if str(attr_name) not in mcs_dict:
                    raise TypeError(f"Class {name} must define an '{attr_name}' attribute. {mcs_dict}")
                # If the attribute may take any type, we don't need to check for its type.
                if attr_type not in [Any, 'any', 'Any']:
                    # But if it's not defined as an attribute with type 'Any', we need to an actual type to check for.
                    if not isinstance(attr_type, type):
                        raise TypeError(f"Class {name}'s '{attr_name}' was declared with an invalid type: {attr_type}.")
                    if not isinstance(mcs_dict[attr_name], attr_type):
                        raise TypeError(f"Class {name}'s '{attr_name}' attribute must be a {attr_type.__name__}.")

            # We don't need to check for mandatory methods in the HCI base class, because it's an abstract class.
        return super().__new__(mcs, name, bases, mcs_dict)

    def __init__(cls, name, bases, cls_dict):
        # The _event_trigger_map is used by the event_trigger decorator to register event triggers to the HCI class.
        # It is a dictionary that maps event trigger names to the methods that implement them.
        # We must check the type of this attribute here, to make sure that the decorator can use it.
        mandatory_instance_attributes = {'_event_trigger_map': dict,
                                         'element_id': Any,
                                         'api': Any,
                                         'ext_id': Any,
                                         'ext_id_type': Any
                                         }
        if bases:
            for attr_name, attr_type in mandatory_instance_attributes.items():
                if str(attr_name) not in cls_dict:
                    raise TypeError(f"Class {name} must define an '{attr_name}' attribute. {cls_dict}")
                # If the attribute may take any type, we don't need to check for its type.
                if attr_type not in [Any, 'any', 'Any']:
                    # But if it's not defined as an attribute with type 'Any', we need to an actual type to check for.
                    if not isinstance(attr_type, type):
                        raise TypeError(f"Class {name}'s '{attr_name}' was declared with an invalid type: {attr_type}.")
                    if not isinstance(cls_dict[attr_name], attr_type):
                        raise TypeError(f"Class {name}'s '{attr_name}' attribute must be a {attr_type.__name__}.")
        super().__init__(name, bases, cls_dict)


class HCIBase(metaclass=HCIMeta):
    """
    Base class for HCI interactions. All HCI classes should inherit from this class.
    The HCI classes are responsible for interacting with the SUT's GUI, CLI or APIs.
    """
    _event_trigger_map = {}

    @classmethod  # This is a class method instead of an abstract method to provide a default implementation.
    def register_event_trigger(cls, event_trigger_name):
        """
        Registers an event trigger to the HCI class. This method is called by the method associated with the
        event trigger name if the decorator :py:func:`event_trigger` is used.

        :param event_trigger_name: The name of the event trigger to be registered.
        """

        def decorator(func):
            cls._event_trigger_map[event_trigger_name] = func
            return func

        return decorator

    @abstractmethod
    def manifest(self):
        """
        Manifests the HCI element of the SUT. This method must implement an SUT-specific way of accessing the
        GUI, CLI or API to get the actual SUT element.
        """
        pass

    @classmethod
    def trigger_event(cls, event_trigger_name, event_trigger_params=None):
        """
        Triggers an event on the HCI element of the SUT. This method must implement an SUT-specific way of accessing
        the GUI, CLI or API to trigger the event.

        :param event_trigger_params:  The parameters to be passed to the event trigger.
        :param event_trigger_name:  The name of the event to be triggered.
        """
        if event_trigger_params:
            if isinstance(event_trigger_params, list):
                event_return = cls._event_trigger_map[event_trigger_name](cls, *event_trigger_params)
            elif isinstance(event_trigger_params, dict):
                event_return = cls._event_trigger_map[event_trigger_name](cls, **event_trigger_params)
            else:
                event_return = cls._event_trigger_map[event_trigger_name](cls, event_trigger_params)
        else:
            event_return = cls._event_trigger_map[event_trigger_name](cls)
        return event_return
