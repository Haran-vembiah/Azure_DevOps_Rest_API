from typing import Union, Dict, Any


class Config:
    full_config: Dict = None
    active_profile: Dict = None
    active_profile_name: str = None
    all_profile_names: Dict = None

    @classmethod
    def set_active_profile(cls, profile_name: str):
        """
        Sets the active profile in the context. This profile will be used to configure the logger and the context data.
        :param profile_name: The name of the profile to activate.
        :type profile_name: str
        :return:
        """
        if cls.full_config is None:
            raise ValueError("The full configuration must be set before activating a profile.")
        if profile_name not in cls.full_config:
            raise ValueError(f"Profile not found in configuration: {profile_name}")
        cls.active_profile_name = profile_name
        cls.active_profile.update({"database": cls.full_config[profile_name]["database"]})

    @classmethod
    def set_full_config(cls, config: Dict):
        """
        Sets the full configuration in the context. This configuration will be used to configure the logger and the
        context data.
        :param config: The full configuration.
        :type config: dict
        :return:
        """
        pass


def put(item: Any, metadata: Dict = None, address: Union[str, Dict] = None):
    """
    Insert or update a data item in the context data. If the item already exists, it will be updated. If it does not
    exist, it will be inserted.

    In practice, items in the context data can also be modified directly.
    However, this function is provided to allow the item to be modified without knowing the address or the internal
    structure of the context data.

    :param item: Any data item.
    :param metadata: A dictionary of metadata describing the item. This metadata will be used to create a record in the
                        context data in the correct place.
    :param address: If the target location of the item in the context data is known, it can be specified here. If the
                    location is not known, the metadata will be used to determine the location. The address can be
                    either an address string returned by this function, or a forward slash delimited string.
    :return:
    """


def get(metadata: Dict = None, address: Union[str, Dict] = None) -> Any:
    pass
