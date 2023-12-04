
[[_TOC_]]

---
## Static analysis Overview

In computer programming, lint or lint-like tools perform static source code analysis, checking for symantec discrepancies.
“Linting” means running a basic quality tool against your code. The tool will check your code syntax and provide instructions on how to clean it.

**Why is “linting” important, and why should we use it?**
One simple reason: linting helps to prevent bugs in your program. In other words:
- Linting makes you a better developer by helping you write better code (checking against coding standards)
- It helps prevent things like syntax errors, typos, bad formatting, incorrect styling, etc
- It saves our time as a developer
- If you are working in a team, it saves time for people who are reviewing your code (no need to distrust for typos and formatting issues)
- It is easy to use
- Lint-like tools usually very easy to set up
- It is free

During the evaluation of static code analysis tool, considered tools **PyCharm - Inspection, Pylint, Prospector and Flake8**. With the advantages of Flake8,decided to go with **Flake8**.

---
### Flake8
Flake8 is a Python library that wraps PyFlakes, pycodestyle and Ned Batchelder’s McCabe script. It is a great toolkit for checking your code base against coding style (PEP8), programming errors (like “library imported but unused” and “Undefined name”).
It has a low rate of false positives.

You can easily add it to your python IDE or editor ( e.g., PyCharm, SublimeText, etc.).
Flake8 runs all the tools by launching the single flake8 command.

**_Note_**: It is very important to install Flake8 on the correct version of Python for your needs. If you want Flake8 to properly parse new language features in Python 3.5 (for example), you need it to be installed on 3.5 for Flake8 to understand those features. In many ways, Flake8 is tied to the version of Python on which it runs.

---
### Flake8 plugins

Flake8 can also be configured with some flake8 plugins.
- [flake8](https://pypi.org/project/flake8/) - Flake8 is a wrapper around these tools(PyFlakes, pycodestyle, McCabe)
- [flake8-builtins](https://pypi.org/project/flake8-builtins/) - Check for python builtins being used as variables or parameters.
- [flake8-bugbear](https://pypi.org/project/flake8-bugbear/) - A plugin for flake8 finding likely bugs and design problems in your program. Contains warnings that don’t belong in pyflakes and pycodestyle:
- [flake8-return](https://pypi.org/project/flake8-return/) - Flake8 plugin that checks return values.
- [flake8-comprehensions](https://pypi.org/project/flake8-comprehensions/) - A flake8 plugin that helps you write better list/set/dict comprehensions.
- [flake8-print](https://pypi.org/project/flake8-print/) - Check for Print statements in python files.
- [Cohesion](https://pypi.org/project/cohesion/) - Cohesion is a tool for measuring Python class cohesion.
- [flake8-cognitive-complexity](https://pypi.org/project/flake8-cognitive-complexity/) - An extension for flake8 that validates cognitive functions complexity.
- [flake8-expression-complexity](https://pypi.org/project/flake8-expression-complexity/) - An extension for flake8 that validates expression complexity.
- [flake8-functions](https://pypi.org/project/flake8-functions/) - An extension for flake8 to report on issues with functions.
- [flake8-eradicate](https://pypi.org/project/flake8-eradicate/) - flake8 plugin to find commented out (or so called "dead") code.
- [flake8-pytest-style](https://pypi.org/project/flake8-pytest-style/) - A flake8 plugin checking common style issues or inconsistencies with pytest-based tests.
- [flake8-docstrings](https://pypi.org/project/flake8-docstrings/) - A simple module that adds an extension for the fantastic pydocstyle tool to flake8.
- [flake8-json](https://pypi.org/project/flake8-json/) - This is a plugin for Flake8 that will format the output as JSON. By default, the output is not pretty-printed.


---
### Installation
Flake8 plugins are all pip packages.
We can easily install the plugins as (ex.) **pip install packagename**

---
### Configuration
Flake8 supports storing its configuration in the following places:
- In top-level user directory
- Can be configured in one of setup.cfg, tox.ini, or .flake8.
- In our project configurations are available in tox.ini.
- To know more details on the current configuration refer tox.ini which is available in project root directory.

Values set at the command line have the highest priority, then those in the project configuration file, then those in your user directory, and finally there are the defaults. However, there are additional command line options which can alter this.
[flake8 configuration](https://flake8.pycqa.org/en/3.9.2/user/configuration.html#), 
[Full Listing of Options in configuration](https://flake8.pycqa.org/en/3.9.2/user/options.html)

### Sample output
- Sample [report file](flake8_sample_report.json) in json format