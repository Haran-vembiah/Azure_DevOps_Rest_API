import argparse

parser = argparse.ArgumentParser(
    prog="runner",
    description="Run automated tests with the Orion Test Automation Framework",
    epilog="For more details please refer to the documentation either on the Azure DevOps Wiki, or its Git "
           "repository."
)

parser.add_argument(
    # The default sut name (or any sut name) must be the same in the terminal pipeline, the TAF database and here.
    '-s', '--sut', default='ti_simulation',
    help="The SUT's sha256 instance ID from the TAF database, "
         "the SUT name (in which case the latest version will be used), "
         "or a shortcut name, such as 'new', to install a new instance of an SUT known to the TAF."
)
parser.add_argument(
    '-t', '--test-set', nargs='+', default='guess',
    help="A list of test suite IDs or the name of a test suite 'group', such as 'ci' to run the CI tests. "
         "If it's 'guess', or not passed at all, the framework will try to guess based on the Build Reason."
)
parser.add_argument(
    '-c', '--config', help="The profile name from the configuration file to use for test execution.")
parser.add_argument(
    '-l', '--log-level', default='WARNING', help="The log level to use for test execution."
)
parser.add_argument(
    '-m', '--run-mode', help="The run mode to use for test execution. "
                             "This also impacts the tolerance level for errors and exceptions. "
)


def get_args():
    return parser.parse_args()