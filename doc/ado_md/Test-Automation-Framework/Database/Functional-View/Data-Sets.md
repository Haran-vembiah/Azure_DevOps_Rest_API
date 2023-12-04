# Introduction

The test automation framework stores all test data in a PostgreSQL database.
In PostgreSQL v14, new data types were introduced, which allowed us to switch to a much more 
flexible data model. Previously the only way to define data sets in the test automation framework was using 
the EAV: Entity-Attribute-Value model. This model is very flexible, but it's also very difficult to query,
and even more difficult to make sure that the data is consistent.

With the introduction of the natively managed JSON data type in PostgreSQL, the data sets can now be defined as JSON documents.
Furthermore, since the data sets are defined in a hierarchical structure like JSON, that maps almost one-to-one
to Python dictionaries, the same data sets can also be 'pickled' and stored in the database as binary data.

For backwards compatibility, the EAV model is still supported, but the new JSON model is the preferred way, 
and the EAV model will be deprecated in the future.

The new tables for storing the data sets are in the 'test' schema:
- test.data_set_base
- test.data_set_json
- test.data_set_bin
- test.data_set_eav

The 'test.data_set_base' table stores identification and metadata for the tables holding the actual data sets.
This data consists of and ID, a name, a description and a JSON document with the type-specific attributes of 
the data set.

The 'test.data_set_json' table holds the data sets as JSON documents.
The 'test.data_set_bin' table holds the data sets as binary data.
The 'test.data_set_eav' table holds the data sets as EAV documents.

The tables holding the data sets in JSON and binary format have a common characteristic.
Each record in the table may correspond to a single record (a single row) 
in the data set, or it may correspond to an entire data set, in which case there is only one record, 
with the ID set to 0. (Not NULL, but Zero)
 
# Data Set Types
What's slightly unorthodox in our solution is that the data sets are a multipurpose resource.
They are used as:
- Test input data (duh)
- Part of the Verification Point definitions in the: 
  - Entry criteria
  - Expected results

To allow the data sets to be used in this way, they can be defined not only as key-value pairs, 
where the values are fixed, but also as key-value pairs where the values are defined as a constraints or rules.

## Value-based data sets
Let's say we have to test a user management system. One of the screens lists the users' details.
The fields to be displayed are:

| Field name      | Data Type        | Allowed Value Range                |
|-----------------|-----------------|------------------------------------|
| Username        | String (varchar) | Alphanumeric characters            |
| Full Name       | String (varchar) | Any text                           |
| Group           | String (varchar) | "Admin" or "User"                   |
| Blocked         | Boolean         | "Yes" or "No"                      |
| Last Login Time | DateTime        | Date and time in yyyy-mm-dd hh:mm:ss format |

To test this feature, a traditional input test data set might look like this:

| Username  | Full Name      | Group | Blocked | Last Login Time     |
|-----------|:---------------|:------|:--------|:--------------------|
| jdoe123   | John Doe       | Admin | No      | 2022-05-15 09:23:41 |
| lsmith    | Lisa Smith     | User  | Yes     | 2022-07-28 17:56:12 |
| mjohnson  | Mark Johnson   | User  | No      | 2022-09-10 14:35:27 |
| abrown    | Anna Brown     | Admin | No      | 2022-06-02 08:12:59 |
| kwilliams | Karen Williams | User  | Yes     | 2022-08-18 12:40:04 |

This is also how a data set is defined in our framework when it's meant to be used as test input data,
and the same data set can also be used as part of the verification point definitions.

## Constraint-based data sets
When a data set is meant to be used as part of the verification point definitions,
some more flexibility with the values might be required. 
That is why the values can also be defined as constraints or rules. 
(The syntax here is for demonstration purposes only, the actual syntax is described in detail later on.)

| Username       | Full Name                 | Group       | Blocked  | Last Login Time                                             |
|----------------|:--------------------------|:------------|:---------|:------------------------------------------------------------|
| ^[A-Za-z0-9]+$ | ^[A-Z][a-z]+[A-Z][a-z]+$  | ^[A-Za-z]+$ | (Yes/No) | **Between** 2022-01-01 00:00:01 **and** 2022-01-01 00:00:01 |

The example here is quite liberal. It allows pretty much any value that each field can hold. 
The only exception is the "Last Login Time" field, where the range is somewhat limited.

This example is also quite simple, but a bit more restrictive than the previous one, and it has multiple options.

| Username          | Full Name                | Group         | Blocked | Last Login Time                                             |
|-------------------|:-------------------------|:--------------|:--------|:------------------------------------------------------------|
| abrown            | ^A[a-z]+Brown$           | Admin         | No      | **Between** 2020-01-01 00:00:01 **and** 2020-12-31 23:59:59 |
| kwilliams         | Karen Williams           | [User, Admin] | Yes     | 2022-08-18 12:40:04                                         |

This data set could be interpreted the following way:
- If the username is 'abrown', the full name must start with 'A', followed by at least one lowercase letter, and end with 'Brown'.
- If the username is 'abrown', the group must be 'Admin'.
- If the username is 'abrown', the user must not be blocked.
- If the username is 'abrown', the last login time must be between 2020-01-01 00:00:01 and 2020-12-31 23:59:59.
- If the username is 'kwilliams', the full name must be 'Karen Williams'.
- If the username is 'kwilliams', the group must be either 'User' or 'Admin'.
- If the username is 'kwilliams', the user must be blocked.
- If the username is 'kwilliams', the last login time must be 2022-08-18 12:40:04.

This last example was meant to demonstrate two characteristics of how the data sets are evaluated when used as 
entry criteria or expected results in verification point definitions:
1. The values in the data set are **conditions**, and the relation between them is "AND".
2. Each row (a.k.a record) in the data set is evaluated separately, and the relation between the rows is "OR".

The first characteristic means that all the conditions in a row must be met for the row to be considered valid.
The second characteristic means that if any of the rows is valid, the entry or exit criteria of 
the verification point is considered valid.


# Data Set Definition
## Value-based data sets
The traditional way of defining data sets, which are meant to be used as test input data, is fairly straight-forward.
1. Create an entry in the 'test.data_set_base' table.
3. Create a corresponding entry in the 'test.data_set_json' table.
4. Create your data set as a JSON document manually, or as a Python dictionary from code.
5. Decide if the data set should be stored per record or per data set.
6. If the data set should be stored per record, create a record in the 'test.data_set_json' table for each record in the data set.
7. If the data set should be stored per data set, create a single record in the 'test.data_set_json' table, with the ID set to 0.

Example value-based data set with 2 records
``` json
{
  '1': {'User_name': 'pilgrim',
        'Full_name': 'Billy Pilgrim',
        'Groups': ['Administrators'],
        'Reset_password': True,
        'Enforce_password_change': True,
        'Deactivate_user': False,
        'Created_by': 'admin-8',
        'Creation_time': '05.06.2023 09:53:04',
        'Modified_by': None,
        'Last_modification_time': '05.06.2023 09:53:04'
  },
  '2': {'User_name': 'trout',
        'Full_name': 'Kilgore Trout',
        'Groups': ['Administrators', 
                    'Assistans', 
                    'Chemists', 
                    'Lab managers', 
                    'Operators'],
        'Reset_password': False,
        'Enforce_password_change': False,
        'Deactivate_user': False,
        'Created_by': 'admin-8',
        'Creation_time': '05.06.2023 09:53:04',
        'Modified_by': None,
        'Last_modification_time': '06.06.2023 09:53'
  }
}
```

The available data types for the parameters included in a data set are discussed on the 
[Parameters](/Test-Automation-Framework/Database/Functional-View/Parameters) page.


## Constraint-based data sets
With the constraint-based (or rule-based) data sets, the values of the parameters are not static, and
they cannot be used as test input data on their own. These data sets can be used as 'context'; entry and exit criteria 
for Verification Points.

The steps to create a constraint-based data set are the same as for a value-based one, the real
difference is in the content. 
Instead of explicitly assigning a fixed value to each parameter, each of them can be associated
with a constraint that defines the acceptable values for that specific parameter.

The following types of constraints are implemented in the test automation framework:
- *regex*: A regular expression is used to define the valid values of a string parameter.
- *list*: A list of allowed values must be provided, and during evaluation, the input value must match one of the items on the list **exactly**
- *eq*: "Equals to". Exact match, must be the same data type at the moment, some casting logic will be implemented later. 
- *range*: Numeric and date values can be accepted within a defined range. 

Constraint types currently in development:
- *domain*: The data set itself does not hold any restrictions on the valid values. Instead, the already configured domain of the parameter (or one of its instances) is applied to the input values.
- *python*: A python expression can be stored in the database and evaluated at runtime. This is an extremely unsecure solution unless the input is properly validated and sanitized. And even then, it is still unsafe.

Example:
``` json
{
  '1': {'User_name': {'constraint_type': 'regex', 'constraint_expression': '^[a-z0-9_-]{3,15}$'},
        'Full_name': {'constraint_type': 'regex', 'constraint_expression': '^[a-zA-Z0-9_-]{3,15}$'},
        'Groups': {'constraint_type': 'list', 'constraint_expression': ['Administrators', 'Assistants']},
        'Reset_password': {'constraint_type': 'list', 'constraint_expression': [True, False]},
        'Enforce_password_change': {'constraint_type': 'list', 'constraint_expression': [False]},
        'Deactivate_user': {'constraint_type': 'eq', 'constraint_expression': True},
        'Created_by': {'constraint_type': 'eq', 'constraint_expression': 'admin-8'},
        'Creation_time': {'constraint_type': 'range',
                          'constraint_expression': ['05.06.2023 09:53:04', '06.06.2023 09:53:04']},
        'Modified_by': {'constraint_type': 'eq', 'constraint_expression': 'admin-8'},
        'Last_modification_time': {'constraint_type': 'eq',
                                   'constraint_expression': '05.06.2023 09:53:04'}
        }
}
```
