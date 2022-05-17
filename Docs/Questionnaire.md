# Basic concepts

## What is a Coding Dojo?
Coding Dojo is a movement promoted by Dave Thomas, which consists of a friendly meeting where a group of programmers get together to improve their skills by completing a programming challenge. This is done in a room with enough seats, at least 1 computer and a projector.

Regardless of your skill level, it is welcome as it is used to foster new skills.

## Difference between Requirements, Acceptance Criteria and Test Scenarios
A requirement is a property that must be present in a system, module, component, etc. whose purpose is to solve a problem in the real world. These must be verifiable either as functional or non-functional requirements.

The acceptance criteria are those that meet the verifiable part of the requirement and tell us if the correct implementation of this requirement has been met.

In a large percentage these criteria are not sufficiently detailed in practice, that is where the test scenarios come in with concrete examples of input and output.

- **Example of requirements** \
 **Req-1:**  As a customer, I want to log in to the virtual store to find out about my orders.
- **Example of acceptance criteria** 
  - **Cri-1-1:** The user must be registered in the virtual store 
  - **Cri-1-2:** The user must log in with a unique username 
  - **Cri-1-3:** The user must log in with a password of at least 10 characters
  - **Cri-1-4:** The username and password must be correct to log in 
  - **Cri-1-5:** The logged in user will not be able to see data that does not belong to him 
- **Example test scenarios** 
  - **Sce-1-4-1:** The behavior of the application by entering a valid username and invalid password.
  - **Sce-1-4-2:** The behavior of the application by entering an invalid username and valid password.
  - **Sce-1-4-3:** The behavior of the application by entering an invalid username and invalid password.                                                                                  

## Examples of non-functional requirements
1. The system must be capable of operating correctly with up to 30,000 users with concurrent sessions.
- **Category :** Performance
2. A backup of the system data must be performed every 48 hours. Backups should be stored in a secure location other than the system location.
- **Category :** Security

## What is TDD?
(Test-Driven Development) It is a form of programming that consists of translating the requirements into tests, which are mostly unitary, it is verified that this test fails (Because if it fails we will know that it works and that it will not throw false positives) and it is implemented the code that makes the test pass successfully, then the written code is refactored in a way that we make sure that it is a clean code and that it works according to the requirements.

The tests must be small, implementing the minimum possible code so that we can easily recognize the origin of the error when one of these tests does not pass correctly.

## What are automated unit tests?
It is a software testing method that consists of small sections of code rigorously analyzed to guarantee its functionality. We have the possibility to write them in a separate program intended for testing.

Automated unit tests also work as documentation by helping to understand how each unit of code works by seeing the results of its interaction with the system.

## What was the first unit testing framework and for which language was it created?
En 1994 kent Back creó el entorno de prueba SUnit para el para el lenguaje smalltask, posteriormente en 1997 junto a Erich Gamma crearon JUnit para el lenguaje Java.
JUnit
- **Date:** 1997
- **Creator:** Erich Gamma and Kent Beck
- **Language:** Java

## Describe the components of the xUnit architecture
- **Test Runner** \
Program that runs tests implemented using the xUnit framework and reports their results.

- **Test Case** \
Class that all unit tests inherit

- **Test fixtures** \
Grouping of preconditions or state necessary to run a test. The developer must know what the exact state is before running the test in order to return after the test has been executed.

- **Test suite** \
It is a suit or group of tests that share the same fixture.

- **Test run** \
  Running a test from setup to cleanup.

- **Test result format** \
It provides a simple, human-readable format, in many cases producing XML output.

- **Assertions** \
Expresses a logical condition that is true for the expected results of a well-functioning system or module. If a failure occurs, an exception is thrown that aborts the execution of the current test.

![Diagram components of the xUnit architecture](https://chrisdaley.biz/images/architecture.png)

## List at least three disadvantages of automated unit tests
1. They cover a lot of time.
2. If your tests aren't very thorough, you might think everything works because the tests pass giving you false assurance that everything is fine.
3. Team members must know how to perform them.
4. In some cases the designs are not 100% confirmed or there are changes as we develop, this inconvenience forces us to redo the tests, which means a waste of time. So it is advisable to start with the tests until you have a specific design in mind.
5. Increased tool needs.
## List at least three benefits of automated unit testing
1. The time invested is recovered by reducing the impact in the future.
2. Improve code quality.
3. A backup is created for future modifications.They also play the role of documentation.
4. They discover errors that we did not see in the development part.


