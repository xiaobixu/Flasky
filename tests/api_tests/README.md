# API Testing for Signant Health Demo Web App #

## Test Product
This suite contains simple API testing for the Signant Health demo web app.  

## Test Scope
The scope of this project is limited to the API testing of the features described in the following session of this document. 

## Test Environment
Please read reqirements.txt under /tests for the required packages information. The browser is Chrome.

## Test Limitations and Risk
The delete mothod could not work yet, it would be better to remove all the user data created during the test in tear down stage. 

## Users
API cosumers

## Test cases:
 1. Register new users
 2. Review users registered in system
 3. Get personal information of users, if authenticated
 4. Update personal information of users, if authenticated

## How to run the test
1. Make the demo app running as background. For further instructions, please read: https://github.com/xiaobixu/Flasky/blob/master/README.md
2. Have all the required liabraries/packages install, for example:
> pip3 install -r ../requirements.txt
4. to run the test:
> python3 test_run.py > reports.txt

## Test result
The test report could be found in reports.txt

## Issues/bugs 
According to the report, 4/4 of test cases pass this time.
