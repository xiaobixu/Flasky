# Automated UI Testing for Signant Health Demo Web App with Robot Framework #

## Test Product
This suite contains simple UI testing for the Signant Health demo web app.  

## Test Scope
The scope of this project is limited to the functional testing of the features described in the following session of this document. 
Non-functional testing, like performance and stress testing, is out of this scope.

## Test Environment
Please read reqirements.txt under ../tests for the required packages information. The browser is Chrome.

## Test Limitations and Risk
N/A

## Users
UI user

## Test cases:
 1. Register through web portal
 2. Review user information from the main view after logged in

## How to run the test
1. Make the demo app running as background. For further instructions, please read: https://github.com/xiaobixu/Flasky/blob/master/README.md
2. Have all the required liabraries/packages install, for example:
> pip3 install -r ../requirements.txt
4. to run the test:
> robot ui_test.robot

## Test result
The test results could be found in the files of report.html

## Issues/bugs 
According to the report, 2/2 of test cases pass on 23.11.2021.
