from pathlib import Path
from tdk.utils import get_asset_path, find_project_root_dir
import logging
from tests.conftest import *


def test_get_asset_path():
    import tdk
    base_path = Path(tdk.utils.__file__).resolve().parent
    config_path = get_asset_path("assets/default_config.json")
    assert config_path == base_path / "assets/default_config.json"


@pytest.mark.parametrize("root_path, relative_path, expected_path, expected_result", [
    ("utils", "assets/default_config.json", "assets/default_config.json", "match"),
    ("root", "assets/default_config.json", "assets/default_config.json", "match"),
    ("cwd", "assets/default_config.json", "assets/default_config.json", "mismatch"),
])
def test_get_asset_paths_dev(root_path, relative_path, expected_path, expected_result):
    import tdk
    if root_path == "cwd":
        base_path = Path.cwd()
        logging.info(f"cwd: {base_path}")
    elif root_path == "utils":
        base_path = Path(tdk.utils.__file__).parent
    elif root_path == "root":
        base_path = find_project_root_dir(Path(__file__))
        logging.info(f"root: {base_path}")
    else:
        raise ValueError("Unsupported root_path")
    config_path = get_asset_path(relative_path)
    logging.info(f"config_path: {config_path} - expected_path: {base_path / expected_path} "
                 f"- Expecting a(n) {expected_result}")

    if expected_result == "match":
        assert config_path == Path(base_path / expected_path).resolve()
    elif expected_result == "mismatch":
        assert config_path != Path(base_path / expected_path).resolve()

