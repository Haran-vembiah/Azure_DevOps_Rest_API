import os
import sys
from typing import Union
from pathlib import Path
import logging


def find_project_root_dir(current_dir: Path = None) -> Union[Path, None]:
    """
    Finds the project root directory by looking for the .git directory, setup.py or pyproject.toml files
    in the current directory and its parents.

    :param current_dir: The current directory to start the search from.
    :type current_dir: pathlib.Path
    :return: The project root directory, or None if it was not found.
    :rtype: pathlib.Path or None
    """
    if current_dir is None:
        current_dir = Path.cwd()
    logging.info(f"Searching for project root directory starting from {current_dir}")
    for parent in current_dir.parents:
        if (parent / "pyproject.toml").exists() or (parent / "setup.py").exists() or (parent / ".git").exists():
            return parent
    logging.warning(f"Project root directory not found")
    return None


def get_asset_path(relative_path: Union[str, os.PathLike, Path]):
    """
    Returns the absolute path to an asset file, given a relative path.
    The relative path is first matched against the application path, then the project root directory.
    :param relative_path:
    :return:
    """
    # First let's check if the path is absolute, if so, we'll just return it
    if not isinstance(relative_path, Path):
        # Convert to Path object. We let the exception propagate if this fails, no try/except here.
        relative_path = Path(relative_path)

    if relative_path.is_absolute():
        if not relative_path.exists():
            raise FileNotFoundError(f"Path not found: {relative_path}")

    # First we try to match the relative path to the application path.
    # The application path is the directory where the executable is located when running in production.
    if getattr(sys, 'frozen', False):
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller >= 1.6
            application_path = Path(sys._MEIPASS)
        else:
            application_path = Path(sys.executable).parent
    else:
        # This means that we are running in development mode, or at least not packaged with PyInstaller
        # We'll assume that the path is relative to the current working directory
        application_path = Path.cwd()
    asset_path = Path(application_path / relative_path)
    # If the path exists, we'll return it
    if asset_path.exists():
        return asset_path
    else:
        # Last resort, we'll try to find the path relative to the project root directory
        project_root_dir = find_project_root_dir(Path(__file__))
        asset_path = Path(project_root_dir / relative_path)
        if asset_path.exists():
            return asset_path
        else:
            raise FileNotFoundError(f"Path not found: {relative_path}")

