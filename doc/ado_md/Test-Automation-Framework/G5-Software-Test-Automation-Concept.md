
[[_TOC_]]


# Introduction
As part of the Orion project, a new software test automation framework will be implemented to speed up and strengthen the quality assurance efforts. This document serves as a high level overview of what can and cannot be expected from the new solution.

To better understand the goals and approach of the test automation concept, it's useful to know the rationale behind them.

- Understand the limitations of 'test' automation.
Technically, software testing consists of at least two types of activities; verification and validation, but only the former can be automated, while the latter brings in the greater value, through interactive (manual) testing.

- Automation is the means, not the ends
Simply because it is _possible_ to automate certain verification points and/or activities, it doesn't mean they _should_ be automated. There are many aspects to consider while selecting test scenarios or verification points to automate, as those must be implemented and maintained, and therefore they have a cost.

- Automated tests must add value.
Seeking out the potential points of failure which aren't feasible to test manually and focusing the automation efforts around these areas is much more likely to help in gauging the software quality, than simply having manual test cases repeated by scripts.

# Goals

The overall goal is to implement a software test automation framework which can be adapted and extended by future G5 instrument development projects. 
To achieve this goal, the new framework has to be [scalable](#scalability), [flexible](#flexibility) and [easy to maintain](#maintainability), while still supporting test and requirement [traceability](#traceability).


## Scalability
Since the Orion project is following an incremental development model, the automated test suite must be able to adapt as the number of implemented features grows. 
In terms of test automation, scalability means more than being able to utilize as much or as little of the available resources as needed for optimal execution. As the application under test becomes more mature and stable, some tests will inevitably become less useful, while new ones will become essential to maintaining an overview of the software quality. Therefore scalability is not a strictly computational challenge, but also a matter of operations management.


## Flexibility
Considering that the Orion project is a pilot for the new G5 platform which is planned to provide the building blocks for future development projects, the method of test automation and the design of the automation framework must also be able to handle various types of requirements of future instruments.

## Maintainability
A common problem many test automation projects share is the overwhelming effort required to maintain the bloated test case repositories.
As previously mentioned in connection with scalability, proper grooming plays a major role in the quality of information gained from the automated test suite.
The processes governing the removal and renewal of test cases must be complemented by the design of the automation framework, in making the repository maintenance as painless as possible.

## Traceability
Contrary to popular belief, the primary goal of software testing is not to find bugs, but to provide a comprehensive overview of the quality of the system under test. The most important prerequisite of this goal is traceability, as there is no way to determine if the software behaves as expected without the ability to tell which requirements have been tested and how.
An inherent characteristic of test automation is that the verification points must be very explicit and closely connected to a specific requirement or acceptance criterion, but that doesn't mean that these relationships need no attention. 
It is important that the connection between tests and requirements is well maintained and monitored throughout the SDLC to avoid false test results.

## Accessibility
Automated tests are mostly implemented based on written requirements and specifications, by engineers and testers with a technical background. As a result, important test cases may be overlooked due to assumptions or misinterpretations, because the expected behavior of the application is often straightforward for those stakeholders who are familiar with the business logic, but can be quite confusing for others.

To channel some of the domain expertise into the automated tests, the framework has to be accessible for the technically less inclined users, whose knowledge is deeper in what the application can and will be used for.
An abstraction layer to enable such stakeholders to define tests on a higher level may bring in very valuable know-how and could serve as a tool to find out _what_ should be tested.

Accessibility is also important in another sense. The framework should be reasonably easy to integrate with future G5 projects' automation solutions. Proper documentation and distribution methods are crucial.



# Approach
## Introduction
Test automation can be very beneficial for most types of software development projects, but without the right approach, it can quickly become a burden without delivering any value. 

The approach to software test automation is determined by a number of variables, and which of these variables are relevant is different in each project. 

## Cooperation with the test team
### Testability
Check if the implemented features in any given iteration are testable manually, try to test as much as possible with automation, report on status.
### Dependency check
Represent the test team during sprint plannings. Check the dependencies and the order certain features should be shipped in order for the test team to be able to work efficiently and minimize downtime. Provide workarounds if possible.
### Reporting
Regularly report to the TM.
1. Executed test cases
1. Coverage
1. Features, potential points of failure which cannot be tested automatically.
1. Risks. Potential delays in delivery of new AUT version or some of its features.
### Test data preparation
Prepare large amounts of varied data based on planned scenarios of the test team.
### Regression tests
Take over as much of the regression tests as possible to enable the test team to focus on new features where a 'Black Swan' is more likely to be discovered.
### Coverage analysis

### Smoke tests

## Low level testing

## GUI Tests

## Integration Tests

# Applied methodologies
## Introduction
No single test methodology can cover the many aspects of software quality. As the application matures, different methods might be suitable for different features or requirements.

However, based on the main functionality of a system, it is possible to choose the major test methodologies upon which the more targeted and often changing test methods can be built.

## The Orion Constellation
For the Orion project, a combination of three different yet very much compatible test methodologies will be used.

![Test_Methods_Venn_Clipart_New.png](/.attachments/Test_Methods_Venn_Clipart_New-18498d26-6f8a-4f4a-921a-2996f48597d0.png)

# Test design
## Use Cases
Use cases can be defined by anyone with minimal technical skills. 
1. Test automation engineers should base their use cases on the written requirements to check the E2E flow, and as the AUT grows, should include multiple requirements. It's also a useful method to reduce the number of executed test cases once a feature becomes part of the baseline and only regression test cases should be executed for it.
1. Manual testers may focus on the more realistic, user-like behavior to help find the odd cases, or even to prepare the application for a manual test (getting it into the right state, creating the data etc.) and avoiding repetitive test steps which are only prerequisites in their actual verification/validation.
1. Business users can define use cases to verify that a specific customer application request can be carried out, or to check the current implementation in case they are unsure if what they defined in the requirements (MRD) is really implemented like they meant it, rather than how they said they wanted it.
# Test implementation
# Operation
# Metrics
# Related pages