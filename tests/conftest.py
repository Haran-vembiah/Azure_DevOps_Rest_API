"""

Pytest configuration file for the tests directory. This file is automatically loaded by pytest when running tests.
See https://docs.pytest.org/en/latest/reference.html#configuration-options for more information on pytest
configuration files.

"""

import json
import pytest
import pathlib

test_assets_dir = pathlib.Path(__file__).parent / "shared_test_assets"
proj_assets_dir = pathlib.Path(__file__).parent.parent / "assets"


def sample_config_file(file_format: str = "json", file_valid: bool = True) -> pathlib.Path:
    file_prefix = "valid" if file_valid else "invalid"
    if not test_assets_dir.exists():
        raise FileNotFoundError(f"Test assets directory not found: {test_assets_dir}")
    config_files_dir = test_assets_dir / "config_files"
    if not config_files_dir.exists():
        raise FileNotFoundError(f"Config files directory not found: {config_files_dir}")
    config_file = config_files_dir / f"{file_prefix}_config.{file_format.strip().lower()}"
    if not config_file.exists():
        raise FileNotFoundError(f"Sample config file not found: {config_file}")
    return config_file


@pytest.fixture(scope="module")
def valid_json_config_file():
    return sample_config_file("json", True)


@pytest.fixture(scope="module")
def valid_yaml_config_file():
    return sample_config_file("yaml", True)


@pytest.fixture(scope="module")
def valid_toml_config_file():
    return sample_config_file("toml", True)


@pytest.fixture(scope="module")
def invalid_json_config_file():
    return sample_config_file("json", False)


@pytest.fixture(scope="module")
def invalid_yaml_config_file():
    return sample_config_file("yaml", False)


@pytest.fixture(scope="module")
def invalid_toml_config_file():
    return sample_config_file("toml", False)


@pytest.fixture(scope="module")
def valid_config_json_schema_file():
    if not test_assets_dir.exists():
        raise FileNotFoundError(f"Test assets directory not found: {test_assets_dir}")
    config_files_dir = test_assets_dir / "config_files"
    if not config_files_dir.exists():
        raise FileNotFoundError(f"Config files directory not found: {config_files_dir}")
    config_json_schema = config_files_dir / "valid_config_schema.json"
    return config_json_schema


@pytest.fixture(scope="module")
def valid_config_json_schema(valid_config_json_schema_file):
    if not valid_config_json_schema_file.exists():
        raise FileNotFoundError(f"Valid JSON config schema file not found: {valid_config_json_schema_file}")
    with open(valid_config_json_schema_file, "r") as json_config_schema_file:
        json_config_schema = json.load(json_config_schema_file)
    return json_config_schema


@pytest.fixture(scope="module")
def valid_json_config(valid_json_config_file):
    with open(valid_json_config_file, "r") as json_config_file:
        json_config = json.load(json_config_file)
    return json_config
