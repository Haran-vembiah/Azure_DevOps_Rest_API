from tests.conftest import *
from tdk.config import validate_config
import json


def test_valid_json_config(valid_json_config, valid_config_json_schema):
    """ Test that a valid JSON config file is validated successfully. """
    assert validate_config(valid_json_config, valid_config_json_schema)


def test_invalid_json_config(invalid_json_config_file, valid_config_json_schema):
    """ Test that an invalid JSON config file raises an exception."""
    with open(invalid_json_config_file, "r") as json_config_file:
        json_config = json.load(json_config_file)
    with pytest.raises(ValueError) as excinfo:
        validate_config(json_config, valid_config_json_schema)
        assert "schema" in str(excinfo.value)



