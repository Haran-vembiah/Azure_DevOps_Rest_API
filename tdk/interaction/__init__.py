"""
The interactions package contains methods for communicating with external systems, usually with one of the SUTs.
This is where the low-level, dirty, technical stuff goes. This package plays a middleware role between the SUT and the
test automation framework. There are 4 main subpackages:
- mg: MacGyver package, for unorthodox ways of interacting with external systems, usually with one of the SUTs.
- api: API package, for interacting with the SUT's API.
- ui: UI package, for interacting with the SUT's GUI or CLI.
- abs_hci: Abstract classes for implementing Human-Computer Interactions (HCI) for the SUT. The user of this package
    can use these basic classes for implementing interactions with the SUT's GUI or CLI. Even though the package is
    named "abs_hci", it can be used for implementing interactions using other patterns, like the Strategy pattern,
    or they can be fully ignored and the user can implement their own classes from scratch.
"""



