# Develop and Debug tool for robot framework

Introduction
------------
This tool is based on [Robot Framework](https://robotframework.org/). I used to implement and debug for the robot test with running the whole test script, but it wastes a lot of time.

So this tool could keep running the test scripts on the same browser.

Setup
----------
* Setting the location of chrome browser as environmental variables
* Create an empty folder at **C:\testChrome**

Usage
-----
Adding `-v debug:${True}` when running test's configuration with [robot framework listener](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-examples) by overwrite the `start_suite` method so that we could develop or debug instead of running the whole robot test.