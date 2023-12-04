## Concept
The idea is that the configuration file contains all available options for each resource the test automation framework 
may use:
- Database connections
- Report templates
- Logging configurations
- Input/output paths
- Tool configurations

Then to select which options to use out of all the available ones in each category, the user 
can create a named `profile` within the configuration file. The profile can then be selected 
when running the test automation framework.

## Configuration file
The structure of the configuration file is defined in a JSON schema file. The schema file is
stored in the `assets` package in the code base. The schema file is used to validate the
configuration file before it is used by the test automation framework.

Even though the schema is defined in JSON format, the configuration file itself can be in JSON, YAML, or TOML format.
The validation will still work, because all of these formats can be parsed into a Python dictionary.

A default configuration is also stored in the `assets` package in the code base. This default configuration
cannot be used directly, but it can be used as a template for creating a new configuration file.

During the execution of the test automation framework, the configuration file must be located right next to the
test automation framework executable. The configuration file must be named `config.json`, `config.yaml`, or `config.toml`
depending on which format is used.

## Configuration structure
The configuration file is divided into sections. Each section contains a number of options. The options are
defined in the JSON schema file. The sections are:
- `database_connections`: Database connections
- `reports`: Report templates and configurations
- `logging_profiles`: Logging configurations
- `paths`: Input and output paths
- `tools`: Tool configurations
- `profiles`: Named profiles

### Database connections
The `database_connections` section contains a list of database connections. Each database connection
has a list of attributes required to connect to the database. Each database type has its own set of
attributes. The attributes are defined in the JSON schema file.
Currently the following database configuration are supported:
- `postgresql`
- `sqlite`
- `mysql`
- `mssql`
- `oracle`

📢 Support for the configuration of these database types does not mean that the test automation framework
can connect to these databases. The test automation framework only supports connecting to PostgreSQL and SQLite databases.  
However, adding support for connecting to other databases is relatively easy, thanks to SQLAlchemy.
Code samples for connecting to MSSQL can be found in the mt-anachem-systemtests-framework repository. (It was used to
insert test data into the LabX database for the PoC.)


### Tools
The `tools` section contains a list of tool configurations. What qualifies as a tool is up to the developer.

In the configuration file, each tool can fall into one of two categories:
- executable
- api

It is a good idea to keep the installation details of any external executables, such as the **Squish Server**, 
then access and use it freely from the test automation framework.  

Another example is Azure DevOps, or rather its API.
Even though it's not an executable, it is still a tool that the test automation framework uses.
(Having said that, Azure DevOps could theoretically be configured twice in the configuration file: once as an api, 
once as an executable, for the `az` command line tool.)

#### Executable tools
The `executable` category is for tools that are installed on the system and can be executed from the command line.
It takes the following fields:
- `command`: The command to execute the tool. This can be a path to an executable, or a command that can be executed
  from the command line.
- `cli_options`: A list of command line options that are passed to the tool when it is executed. 
   The definition of each command line option is very similar to that used in Argparse.
  - `name`: The name of the option.
  - `type`: The type of the option. This can be one of the following:
    - `str`
    - `int`
    - `float`
    - `bool`
    - `list`
  - `required`: Whether the option is required or not.
  - `help`: A help text for the option.
  - `choices`: A list of possible values for the option.
- `optional_properties`: A list of optional properties that can be used to configure the tool. Handling these properties
  is up to the developer.

#### API tools
The `api` category is for tools that are accessed through an API. It takes the following fields:
- `url`: The URL of the API.
- `port`: The port used to access the API.
- `authentication_type`: The authentication method used to access the API. The fields required for each authentication
   method are NOT defined in the JSON schema file to allow more flexibility. It is up to the developer to make sure that 
   the authentication method is valid for the tool and that the required fields are defined.


### Report templates and configurations
The configuration file's reports section contains a list of report templates and configurations.
The only required field here is `report_type`. The other fields depend on the report type and
to keep things flexible, the schema file does not define any other fields.
It is the developer's responsibility to make sure that the report template or configuration
is valid for the report type, and that they access the configuration options correctly.


### Logging configurations
The configuration file's logging profiles section contains a list of logging profiles. The only required fields here
are:
- `long_name`: The human-readable name of the logging profile.
- `config`: A dictionary containing the logging configuration. The structure of this dictionary is NOT defined in the
  JSON schema file, due to the high complexity of the logging configuration allowed by dictConfig.

### Input and output paths
These paths can be configured to centralize the locations of the input and output files used by the test automation
framework. This section is very flexible and the schema file does not define any fields. It is up to the developer
to make sure that the paths are valid and that they access the paths correctly.

This is where the log paths, report output paths, and test data paths can be defined. 

Each path will of course have a short name, that is its key in the configuration file. The short name is used to 
access the path from the test automation framework. The properties of each path are:
- `path`: The path itself.
- `description`: A human-readable description of the path.
- `long_name`: A human-readable name of the path.

### Named profiles
The `profiles` section contains a list of named profiles. Each profile contains a list of options that are used
by the test automation framework. The options are defined in the JSON schema file. The options are grouped into
the following sections:
- `databases`: Database connections. Referenced by name from the `database_connections` section. There are two
  types of database connections that need to be configured in the profile: (These two can be the same db connection.)
  - `olap`: The OLAP (Online analytical processing) database connection.
  - `oltp`: The OLTP (Online Transaction Processing) database connection.
- `tools`: Tool configurations. Referenced by name from the `tools` section.
- `reports`: Report templates and configurations. Referenced by name from the `reports` section.
- `logging_profile`: Logging configuration. Referenced by name from the `logging_profiles` section.
- `paths`: Input and output paths. Referenced by name from the `paths` section.