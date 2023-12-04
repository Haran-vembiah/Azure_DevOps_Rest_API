[[_TOC_]]

---
# Test Automation Framework(TAF) Test Execution Flow:
---
## Configuration:
1. It is essential to *set up the command line arguments* needed to run a test using the Test Automation Framework (TAF).
   - For config argument use "-c" or "--config", to set configuration for the test execution using name of the configuration available in config list file. e.x Dev
   - For test suites argument use "-t" or "--test_suites", to specify test suites for the test execution could be a list of test suite IDs or the name of a test set.
     - Make sure the Test set or list of test suites given here are available in TAF DB and mapped with test suites and Test cases.
   - For SUT argument use "-s" or "--sut", to specify the SUT for test execution could be SUT's sha256 instance ID, or the SUT name or new to install a new instance. 
   - For lcm argument use "-x" or "--lcm", to specify the LabX version to use for test execution

2. It _parses the provided command line arguments_ and creates a dictionary of parameters (taf_run_params) for further usage throughout the execution.

3. It checks if a specific configuration has been provided; if not, it uses the default configuration.
   - Based on the value provided on the command line argument "-c" or "--config".

   - _Initializes the TAF_ by reading the configuration file specified by the config argument provided in the command line argument from the list of configuration files available on TAF.
     - Make sure the Configuration files of TAF are available and accessible to get the configuration.

## Initialize TAF Runner:
1. Initializes the *TAF context*, and it creates a dictionary to store context variables.

2. Initializes a *database connection* by creating a new db session with the db name available on the configuration set in command line argument.
   - Database specified in the configuration file should be available for connection.

3. *Starts a Squish server instance* locally if one is not already running on the specified port.
   - Server exe and port number should be available in the configuration and squish server must be installed on the given path.

4. Setting up *TAF logging* based on the type specified in the selected configuration file.
   - Make sure the logging configurations are available in the configuration name given in the command line argument "-c" or "--config".

## Dispatch AUT
1. Finds an existing *SUT instance* or creates a new one and register it with the framework.
   - Retrieves from the TAF DB, If the command line argument "-s" or "--sut" set with a valid SUT's sha256 instance ID or SUT name and the same available in the TAF DB and installed in the test host.
   - If the command line argument "-x" or "--lcm" configured, it gets the LCM instance and initiate the WebDriver to interact with the SUT via browser.
     - LCM instance should be available on the TAF DB
     - If the command line argument "-s" or "--sut" configured as "new"
       - Looks for a SUT release, extract and install and register it with framework along with pipeline, build and Azure DevOps details.
       - Created a local test node.
     - SUT instance set as active SUT.
     - It retrieves the most recently created TestNode object where the node_state is "FREE".
2. Initializes the *test session* with the retrieved test node and creates a Test session with a session ID.
   - Make sure the Test node exists for the active SUT. 
3. The *Test run* is initialized with the Test session ID and Test node ID.
4. *Test suites* are retrieved from the test set given in command line argument "-t" or "--test_suites".
5. *Test set attributes* are retrieved from the TAF database, filtering on the Test set ID and ordering by exec_order.
   - Make sure the Test set attributes are available in the TAF Db for the test set.
6. The *AUT is initialized* by checking the AUT type, retrieving a list of GUI elements from the TAF database,
   - *preconfiguring* the SUT based on test attributes
   - *starting the AUT* with the port number provided on the Test node.
     - Available port number should be configured on the Test node.
## Test execution
1. Tests are executed by *iterating over test suites, Test cases, Test steps, VP(Verification point), and VP instances* and logging the results for each VP instance.
   - Make sure atleast one test case exist for the Test suite 
   - Make sure atleast one test step available for the Test case
   - Make sure atleast one verification point available for the Test step
   - Make sure atleast one VP instance available for the verification point, with the state ENABLED.
     - Make sure the VP instance has entry condition, event to trigger and exit condition to conclude the result of the vp instance.
     - For each event, event object, event type and event function and parameters for the event functions should be available 
     - And each GUI element should have element type and external identifier to identify the element to trigger the event.
## Test Report
1. A test report in HTML format is generated based on the provided test run info for the Test session and TAF configuration.
   - The report contains pipeline details, test environment details, test results summary per requirement, CI test result summary displayed as a stacked chart, and detailed test results.

**visual representation of the execution flow, which can be useful for understanding the sequence of steps involved in executing tests.**

::: mermaid
flowchart TD
A[Set up command line arguments] --> B(Parse provided arguments and create dictionary of parameters)
B --> C(Check if specific configuration is provided)
C -- Yes --> D(Use specified configuration for TAF initialization)
C -- No --> E(Use default configuration for TAF initialization)
D --> F(Read configuration file and store in config_map)
F --> G(Retrieve full configuration details as TAF config)
E --> G
G --> H(Initialize TAF context)
H --> I(Initialize database connection)
I --> J(Start Squish server instance if not already running on specified port)
J --> K(Set up TAF logging)
K --> L(Find existing SUT instance or create new instance and register with framework)
L --> M(Initialize test session with retrieved test node and create session ID)
M --> N(Initialize Test run with session ID and Test node ID)
N --> O(Retrieve test suites from Test set specified in command line argument)
O --> P(Retrieve Test set attributes from TAF database)
P --> Q(Initialize AUT)
Q --> R(Execute tests)
R --> S(Generate test report in HTML format)
subgraph Test Execution

R --> A1[Iterate over test suites] --> B1(Iterate over test cases)
B1 --> C1(Iterate over test steps)
C1 --> D1(Iterate over verification points)
D1 --> E1(Iterate over VP instances)
E1 -- Yes --> F1(Log results for VP instance)
E1 -- No --> E1
F1 --> G1(Repeat for all VP instances)
G1 --> D1
C1 -- No --> C11(End of test case)
C11 --> B11(Repeat for all test cases) --> C1
B11 --> A11(End of test suite)
A11 --> H1(End of all test suites)
end
:::