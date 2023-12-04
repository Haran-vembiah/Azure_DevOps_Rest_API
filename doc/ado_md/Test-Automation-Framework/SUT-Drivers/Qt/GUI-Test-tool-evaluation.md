# Management Summary
This Wiki page describes the GUI test automation tool selection process for the G5 platform.

To spare the un-interested reader from the details, the first chapter; [Summary and recommendation](#summary-and-recommendation) contains the results of the process, and only the [subsequent chapters go into the technical details](#technical-details) 

# Summary and recommendation
## Candidates
The initial list of candidates was composed based on Mettler Toledo's conventions and recommendations by employees, web searches, personal experience and Gartner Inc.'s annual report; [Magic Quadrant for Software Test Automation](https://www.gartner.com/en/documents/3894271/magic-quadrant-for-software-test-automation).

The primary criteria of the evaluation was the automation tools' ability to handle UI elements created with the Qt framework, which significantly narrowed the search. 

|Tool name|Source|Outcome notes|
|--|--|--|
|Froglogic Squish for Qt|Gartner, MT (AutoChem, LabTec, MatChar)|[Recommended solution](#recommended-solution)|
|SmartBear TestComplete|Gartner, Experience|Failed the tests. While it offers some support for Qt interfaces, it is limited to Widgets, but QML and QtQuick objects are not recognized|
|Appium|MT (LabX team)|Failed the tests. Its reliance on the Windows UI Automation framework - which was designed for accessibility, not testing - limits its funcionality. Only certain Qt objects were reconginzed during the tests, mostly with efforts which would burden the developers.|
|Leapwork |web search|Besides being a code-free automation tool, their claim of supporting Qt elements proved to be an exaggeration.|
|Qt Monkey|web search|Could work as a budget solution, but it's an open source tool developed by two contributors, so the platform development would become MT internal responsibility. Not licensed.|
|Qt Test|web search|Failed assessment. Onyl useable on unit-test level|
|KD Executor (Windows port)|web search|Failed assessment. No update since 2005|
|Eggplant|Gartner|Failed assessment. The company is focusing on more fashionable technologies. Licensing difficulties.|
|IBM Rational|Gartner, Experience|Failed assessment. No support for Qt 5 GUI elements.|
|CA Technologies|Gartner|Failed assessment. The company's testing related products are not what we need.|
|MS Visual Studio Test Platform|Gartner|Failed assessment. Meant for unit- and integration tests.|
|Tricentis Tosca|Gartner, Experience|Failed assessment. Tosca is focused on less technical testers (click and drag test case creation), and is yet to improve its capabilities in reliably handling GUI objects.|
|Worksoft Certify|Gartner|Failed assessment. Primarily code-free test automation.|

## Recommended solution
### Key factors
Although Squish offers many useful features, the single most important one in this selection process was its Qt-specific hooking solution. No other tool currently available on the market can handle QML objects with the level of detail and reliability as that of Squish. 

Another comparable tool is SmartBear's TestComplete, which is a leader and overall champion of the GUI test automation tool market, and yet Squish is closely matching its capabilities.

The following list is an overview of Squish's features.
<table>
<tr><th>Feature</th><th>Use</th></tr>
<tr><td>BDD</td><td>Enables non-technical users to define automated test cases and sets, bringing automated verification one step closer to actual testing (i.e. verification & validation)</td></tr>
<tr><td>Object mapping and identification tools</td><td>Although it's a standard feature of most advanced GUI automation tools, Squish implements a very accessible and maintainable solution.</td></tr>
<tr><td>Distributed testing</td><td>Run test sets on a schedule or triggered by events, without supervision and the need for additional licenses.</td></tr>
<tr><td>Visual verifications</td><td rowspan=2>The extensive list of object attributes available through Squish and the visual verification features allow us to perform actual GUI tests, as opposed to functional tests carried out via the GUI.</td></tr>
<tr><td>Detailed object attributes</td></tr>
<tr><td>Image based testing</td><td>Verification of charts and graphs</td></tr>
<tr><td>Data Driven testing</td><td>Rather than creating a test case for each value a parameter can take, the test data can be generated, and Squish can iterate through each combination of values.</td></tr>
<tr><td>Script language support</td><td>Finding a tester with Python, Ruby or JavaScript skills is easy.</td></tr>
<tr><td>Optical character recognition</td><td>Can be a useful feature to find the notorious 'text too long' issues</td></tr>
<tr><td>Reporting</td><td>No need to implement a reporting layer straight away, just to get started.</td></tr>
</table>

Technically not a feature, but a definite plus; there are at least three teams within MT already using Squish, which means in-house community support.

### Pricing
 Named licenses for Froglogic Squish cost EUR2400 each, which includes unlimited installations of Squish servers to allow parallel test execution. 
The price also includes official support and updates for one year. 
If the support and update subscription is not extended at the end of the year, the license remains valid for the last downloaded version of Squish.

----

# Technical Details

This section details the evaluation of various GUI test automation tools for the G5 Platform. A more high-level summary of the process can be found here: [Management Summary](#management-summary))

# Evaluation process
## Information gathering
The first step of the evaluation process was input gathering to define the selection criteria, by answering some generic questions:
- What type of test automation is needed?
- To what extent should the tests be automated?
- Are there any tools already available?
- What are the existing solutions within AnaChem/MTANA/MT?
- What's the technology stack like?
- Is there an existing vision of the test automation solution? 
- What's the budget?

The answers to these question came from 1 on 1 meetings and discussions, intranet and internet searches, and in some cases; from unsolicited advice.

## Selection criteria
Based on the collected information, an incomplete list of criteria was created and roughly prioritized. 
1. Must be able to handle Qt-based GUIs - specifically QtQuick and QML elements.
2. Allow unsupervised test execution in a distributed environment.
3. Has to be scalable.
4. Support for integration into a more complex test automation solution.
5. Support for script languages.
6. Good customer support.
7. Product lifecycle expectations - a long term solution is preferred.
8. Technical support availability - in-house, community and corporate.
9. Built-in features which could help to
    - shorten the test cycle
    - reduce the solution's complexity
    - lighten the workload

## Candidates
The initial list of candidates was composed based on Mettler Toledo's conventions and recommendations by employees, web searches, personal experience and Gartner Inc.'s annual report; [Magic Quadrant for Software Test Automation](https://www.gartner.com/en/documents/3894271/magic-quadrant-for-software-test-automation).

|Tool name|Description|Link|
|--|--|--|
|Froglogic Squish for Qt|The only tool with a Qt-specific hook. Support for BDD, DDT and several script languages|https://www.froglogic.com/squish/|
|SmartBear TestComplete|An excellent, tried-and-true GUI test automation tool sporting all popular test automation features, now powered by AI. Some support for Qt objects. |https://smartbear.com/product/testcomplete/overview/|
|Appium|Selenium for mobile apps. Free and open source. Doesn't hook into any apps on its own, but through on external drivers. Relies on the UI Automation Framework for Windows apps. |http://appium.io/|
|Leapwork |Code-free test automation tool claiming to support Qt applications.|https://www.leapwork.com/product/test-automation|
|Qt Monkey|Qt Monkey is a tool to automate testing of Qt-based applications (widgets only).|https://github.com/Dushistov/qt_monkey|
|Qt Test|The Qt Company's own solution for unit testing|https://doc.qt.io/qt-5/qtest-overview.html|
|KD Executor (Windows port)|A long-abandoned project from the times when Qt was **_the_** GUI creation tool for KDE.|https://www.linux-apps.com/p/1127170/|
|Eggplant|A sophisticated automation tool, mainly targeting the most-hyped technologies.|https://eggplant.io/|
|IBM Rational|IBM's Rational Test Workbench is a heavyweight framework providing solutions for far more than GUI test automation.|https://www.ibm.com/us-en/marketplace/rational-test-workbench|
|CA Technologies|A solution package for various test automation needs, focusing on Agile methodologies|https://www.ca.com/us/products/test-case-design.html|
|MS Visual Studio Test Platform|Microsoft's Unit testing framework, shipped with Visual Studio|https://github.com/microsoft/vstest|
|Tricentis Tosca|No-code GUI test automation tool.|https://www.tricentis.com/products/automate-continuous-testing-tosca/|
|Worksoft Certify|Yet Another Code-free Automation Tool. Certify supports a wide range of technologies and isn't limited to GUI automation.|https://www.worksoft.com/products/worksoft-certify/|

## Assessment

Before any testing could take place, each company/product was assessed based on their product descriptions, mission statements, reviews and target audience.
Those solutions which didn't meet any of the selection criteria and those which clearly targeted a different customer base, technology stack or user type, were eliminated.

|Tool name|Assessment outcome|
|--|--|
|Froglogic Squish for Qt| Moves on to next phase of the evaluation as top contender|
|SmartBear TestComplete| Offers outstanding features and technical support. Reputable company. Qt-compatibility must be tested.|
|Appium|Free and open source. Generic Windows application support. Qt-compatibility to be tested. |
|Leapwork | Besides being a code-free automation tool, their claim of supporting Qt elements proved to be an exaggeration.|
|Qt Monkey|Could work as a budget solution, but it's an open source tool developed by two contributors, so the platform development would become MT internal responsibility. Not licensed.|
|Qt Test|Onyl useable on unit-test level|
|KD Executor (Windows port)|No update since 2005|
|Eggplant|The company is focusing on more fashionable technologies. Licensing difficulties.|
|IBM Rational|No support for Qt 5 GUI elements. The Rational Test Workbench is a too complex solution.|
|CA Technologies|The company's testing related products are not what we need.|
|MS Visual Studio Test Platform| Meant for unit- and integration tests, not a GUI test automation tool.|
|Tricentis Tosca|Tosca is focused on less technical testers (click and drag test case creation), and is yet to improve its capabilities in reliably handling GUI objects.|
|Worksoft Certify|Primarily code-free test automation.|
## Testing
After the assessments only three tools remained in the race. 
1. Appium
2. Squish for Qt
3. TestComplete

These tools were each installed and tested against a prototype Qt application. 

### Process overview
#### The application under test
To be able to test each tool's capability of handling various types of Qt GUI elements, a sample application was built containing a variety of object types. The basis for the application was the new Titrator's GUI prototype, but rather than a consolidated object madel, the sample application used custom elements wherever it was possible, and no instrumentation to help the automation tools in identifying objects.

#### The 'test cases'
There was no predefined set of test cases, as each tool had its own strengths and weaknesses, and so each had a different focus area.
While the method of testing was not identical for each tool, the expectations were the same.
1. Installation
An easy installation process can not only save time, it also helps in making the test automation framework more stable, and hints at the tool's scalability  and distributability.
1. Dependencies
A tool that is self contained is easier to maintain. Any external dependency is a potential risk.
1. Object recognition
A GUI test automation tool's usefulness lies primarily in its ability to recognize and handle elements on the screen.
1. Maintenance needs
Some tools require more maintenance than others to handle changes in the application under test. 
1. Features
Some features can make test automation much more efficient. 

#### Appium tests
##### Installation
The installation process of Appium on a Windows platform is far from convenient, and the corporate proxy and firewall only make it harder. 
1. Install Node.js to get NPM. Guaranteed to run into problems as the installer tries to fetch additional modules from online repositories.
1. Install Appium via NPM. Once again; the proxy must be configured in NPM to avoid issues, but even so, the _appium-doctor_ has to be executed after the half-successful installation and the reported issues must be addressed one-by-one manually. 
![appium_doctor.png](/.attachments/appium_doctor-0e0f548b-c8ff-4ae7-89ae-30e8993e394e.png)
1. Install a client library. The difficulty of this task depends on the client library itself.
1. Switch to Developer mode. Without enabling developer options in Windows, Appium cannot run.
![developer_mode_not_enabled.png](/.attachments/developer_mode_not_enabled-27bfb3bf-37b8-4adf-b74a-6fc297edb7c0.png)
##### Dependencies
Appium is basically a version of Selenium with support for mobile applications. It achieves this additional capability by relying on platform specific frameworks and libraries. 
1. **Windows UI Automation Framework**. Previously known as Windows Accessibility, this framework was meant to provide support for developing applications with easier access. Without it, Appium cannot do anything on its own.
1. **WinAppDriver**. All Appium Windows client libraries rely on this driver, so as long as it's actively developed, there is no problem. How long it will be supported is still a question, given that Windows has given up on its goal of breaking into the mobile phone market and staying there.
1. **Client libraries**. Appium client libraries are maintained by both individuals and corporations, but since these are mostly open source projects, there's no obligation to provide support or to continue development. Once again, since Microsoft gave up on the Windows Phone, there's no guarantee that all of these libraries will be in active development five years from now.
GUI Test Tool Evaluation - Technical Details
##### Object recognition
As Appium relies on the Windows UI Automation Framework, its object recognition capabilites are also limited by it. Standard UI elements are usually recognized, but custom ones - in most cases - fly under the radar.
1. Standard types are recognized ![inspect_screen_1.png](/.attachments/inspect_screen_1-1e6e2ea0-b3a0-42e1-84cf-dbf42e983ab0.png)

1. Some custom types are recognized, and their custom class is also displayed in Inspect.
![inspect_drawer_and_sub_drawer.png](/.attachments/inspect_drawer_and_sub_drawer-4b871641-1bdc-450d-9060-65e192f30b50.png)

1. Some frequently used custom types cannot be discovered by the UI Automation Framework
![inspect_table.png](/.attachments/inspect_table-39dbd0dc-1f70-45e0-b20b-dd03e0cfa238.png)

Recognizing these objects doesn't mean they are identified and available for Appium to be handled reliably, but limited user action simulation is possible.

##### Maintenance
Appium's reliance on the Windows framework means that it can only reference GUI elements directly and repeatably, which have an Automation ID. Dynamic elements always have to be looked up, and only their Runtime ID can be used to access them for imitating user actions, which changes in each run.

Automation IDs must be manually set by the developers, and therefore are an extra task and an unwanted risk to the stability of the automated tests.

##### Features
Appium has no mentionable features.

#### Squish tests
##### Installation
Squish comes with a standard Windows installer: _Next>, Next>, Finish_
No additional software packages or configuration steps are neccessary.
##### Dependencies
Squish is delivered along with all of its dependencies, including the script interpreters. It is possible, however to replace these interpreters with more recent versions or use external libraries, in which case it's the user's responsibility to maintain those.
##### Object recognition
Squish has several variants and the customer can choose based on the technology used to develop the tested application. Each variant is shipped with _hooks_ developed specifically for a given technology.
_Squish for Qt_ is using a library developed for Qt-based applications. 
Froglogic and The Qt Company are cooperating to keep Squish up to date on any changes which might affect its ability to handle Qt objects.
Even with this specialization, Squish - admittedly - fails to handle some GUI elements reliably.
The one example found during the evaluation was the context menu. Though context menus are recognized during test case recording, Squish often fails to identify them during test case execution.

##### Maintenance

##### Features
#### TestComplete tests
##### Installation
TestComplete also comes with a standard Windows installer and requires no additional configuration or software packages.
##### Dependencies
TestComplete is developed entirely by SmartBear and all of its dependencies are handled internally and are delivered with the installation package.
##### Object recognition
TestComplete has limited support for Qt elements. QWidgets are mostly recognized and handled, but when it comes to QtQuick or QML objects, it performs even worse that Appium:

*QWidget and QML applications in TestComplete and Windows Inspect*
![QML_vs_QWidget_application.png](/.attachments/QML_vs_QWidget_application-6d43cd99-fe5b-4d7a-a545-3fb8bc842c51.png)



*QML applications built with and without debug information*
![QML_Examples_TC_vs_Inspect.png](/.attachments/QML_Examples_TC_vs_Inspect-b364de88-68bf-4eeb-87a1-ce0f1d16ad22.png)

##### Maintenance
Since TestComplete failed to recognize QML objects, maintenance tests could not be performed.
##### Features
Even though TestComplete is very feature-rich, since it's not QML-compatible, these checks are out of scope.
### Results