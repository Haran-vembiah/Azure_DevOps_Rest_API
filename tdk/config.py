"""
This module provides functionality for reading, validating, and writing configuration files.
It supports JSON, YAML, and TOML file formats. The module allows easy reading of configuration files into a dictionary,
validation of the configuration against a JSON schema, and writing a configuration dictionary back into a file of any
supported format.
The module uses `pathlib <https://docs.python.org/3/library/pathlib.html>`__ for file access,
ensuring compatibility with various file path representations.
YAML files are handled using `PyYAML <https://pypi.org/project/PyYAML/>`__,
JSON files are handled using the built-in `json <https://docs.python.org/3/library/json.html>`__ module,
and TOML files are parsed using `tomli <https://pypi.org/project/tomli/>`__ and written using
`tomli-w <https://pypi.org/project/tomli-w/>`__, since the O.G. `toml <https://pypi.org/project/toml/>`__
module is not maintained anymore. The `jsonschema <https://pypi.org/project/jsonschema/>`-- module is responsible
for validating the configuration against a JSON schema.

Functions:
    - read_config: Reads and returns the contents of a configuration file.
    - load_json: Loads JSON file contents.
    - load_yaml: Loads YAML file contents.
    - load_toml: Loads TOML file contents.
    - write_config: Writes a configuration dictionary to a file.
    - save_json: Saves a dictionary to a JSON file.
    - save_yaml: Saves a dictionary to a YAML file.
    - save_toml: Saves a dictionary to a TOML file.
    - validate_config: Validates the configuration against a JSON schema.
"""

import json
import yaml
import tomli
import tomli_w
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from pathlib import Path
from typing import Any, Dict, Union


def read_config(file_path):
    """
    Reads a configuration file and returns its content as a dictionary.

    :param file_path: The path to the configuration file.
    :type file_path: str
    :return: A dictionary containing the configuration.
    :rtype: dict
    :raises FileNotFoundError: If the file is not found.
    :raises ValueError: If the file format is unsupported.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")

    if path.suffix in ['.yaml', '.yml']:
        return load_yaml(path)
    elif path.suffix == '.json':
        return load_json(path)
    elif path.suffix in ['.toml', '.tml']:
        return load_toml(path)
    else:
        raise ValueError(f"Unsupported file format {path.suffix}")


def read_schema(file_path):
    """
    Reads a JSON schema file and returns its content as a dictionary.

    :param file_path: The path to the JSON schema file.
    :type file_path: str
    :return: A dictionary containing the JSON schema.
    :rtype: dict
    :raises FileNotFoundError: If the file is not found.
    :raises ValueError: If the file format is unsupported.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Schema file not found: {file_path}")

    if path.suffix == '.json':
        return load_json(path)
    else:
        raise ValueError(f"Unsupported file format {path.suffix}")


def load_json(path):
    """
    Loads a JSON file and returns its content as a dictionary.

    :param path: Path object pointing to the JSON file.
    :type path: Path
    :return: A dictionary containing the JSON file content.
    :rtype: dict
    """
    with open(path, 'r') as file:
        return json.load(file)


def load_yaml(path):
    """
    Loads a YAML file and returns its content as a dictionary.

    :param path: Path object pointing to the YAML file.
    :type path: Path
    :return: A dictionary containing the YAML file content.
    :rtype: dict
    """
    with open(path, 'r') as file:
        return yaml.safe_load(file)


def load_toml(path):
    """
    Loads a TOML file and returns its content as a dictionary.

    :param path: Path object pointing to the TOML file.
    :type path: Path
    :return: A dictionary containing the TOML file content.
    :rtype: dict
    """
    with open(path, 'rb') as file:
        return tomli.load(file)


def write_config(config, file_path):
    """
    Writes a dictionary to a configuration file in JSON, YAML, or TOML format.

    :param config: The configuration dictionary to write.
    :type config: dict
    :param file_path: The path where the configuration file will be written.
    :type file_path: str
    :raises ValueError: If the file format is unsupported.
    """
    path = Path(file_path)
    if path.suffix in ['.yaml', '.yml']:
        save_yaml(config, path)
    elif path.suffix == '.json':
        save_json(config, path)
    elif path.suffix in ['.toml', '.tml']:
        save_toml(config, path)
    else:
        raise ValueError("Unsupported file format")


def save_json(config, path):
    """
    Saves a dictionary to a JSON file.

    :param config: The configuration dictionary to save.
    :type config: dict
    :param path: Path object where the JSON file will be saved.
    :type path: Path
    """
    with open(path, 'w') as file:
        json.dump(config, file, indent=4)


def save_yaml(config, path):
    """
    Saves a dictionary to a YAML file.

    :param config: The configuration dictionary to save.
    :type config: dict
    :param path: Path object where the YAML file will be saved.
    :type path: Path
    """
    with open(path, 'w') as file:
        yaml.dump(config, file)


def save_toml(config, path):
    """
    Saves a dictionary to a TOML file.

    :param config: The configuration dictionary to save.
    :type config: dict
    :param path: Path object where the TOML file will be saved.
    :type path: Path
    """
    with open(path, 'wb') as file:
        tomli_w.dump(config, file)


def validate_config(config, schema):
    """
    Validates a configuration dictionary against a JSON schema.

    :param config: The configuration dictionary to validate.
    :type config: dict
    :param schema: The JSON schema to validate against.
    :type schema: dict
    :raises ValueError: If the configuration does not conform to the schema.
    """
    try:
        validate(instance=config, schema=schema)
    except ValidationError as e:
        raise ValueError(f"The input: {e.path} does not conform to the schema: {e.schema_path}")
    return True


def get_config(config_file: Union[str, Path] = Path("assets/default_config.json"),
               schema_file: Union[str, Path] = Path("assets/config_schema.json")) -> Dict[str, Any]:
    """
    Reads a configuration file, validates it against a JSON schema, and returns the configuration dictionary.

    :param config_file: The path to the configuration file. Defaults to "assets/default_config.json".
    :type config_file: str
    :param schema_file: The path to the JSON schema file. Defaults to "assets/config_schema.json".
    :type schema_file: str
    :return: A dictionary containing the configuration.
    :rtype: dict
    """
    config = read_config(config_file)
    schema = read_schema(schema_file)
    validate_config(config, schema)
    return config
