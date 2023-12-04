"""
This module contains the main entry point for the TDK runner.
"""
from tools.runner import cli
from tdk.config import get_config

if __name__ == '__main__':
    # Load the configuration
    full_config = get_config()
    # Parse and process the command line arguments.
    args = cli.get_args()
    # Activate the selected config profile in the context and configure the logger.

