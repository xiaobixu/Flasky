*** Settings ***
Documentation   This suite contains simple UI test for a web protal, against the following acceptance criterias:
...             1. User can register through web portal
...             2. User can review their own user information on the main view
Library     SeleniumLibrary
Test Teardown   Close All Browsers

*** Variables ***
${url}  http://192.168.1.240:8080/
${browser}      chrome
${username}     xiaobixu
${password}     thisISaPassword
${firstname}    Xiaobi
${familyname}   Xu
${phonenumber}  +35800000000

*** Test Cases ***
User can register via web portal
    [Documentation]  The user can register via the web portal
    Open the main page
    Open the register page from main page
    Enter Username      ${username}
    Enter Password      ${password}
    Enter First name       ${firstname}
    Enter Family name       ${familyname}
    Enter Phone number      ${phonenumber}
    Click on Register button
    The Login page should be opened

User can review their own user information on the main view
    [Documentation]  After log in, the user can view their user information on the main view
    Open the main page
    Open the Login page from main page
    The Login page should be opened
    Enter Username      ${username}
    Enter Password      ${password}
    Click on Log In button
    The user information should be shown correctly on the main view

*** Keywords ***
Open the main page
    Open Browser    ${url}  ${browser}
    Wait Until Page Contains    index page
    Page Should Contain     Demo app
    Page Should Contain     Register
    Page Should Contain     Log In

Open the register page from main page
    Click Element   xpath:/html/body/nav/ul/li[1]/a
    Wait Until Page Contains    Username
    Page Should Contain     Password
    Page Should Contain     First name
    Page Should Contain     Family Name
    Page Should Contain     Phone number
    Page Should Contain Element     xpath:/html/body/section/form/input[6]

Open the Login page from main page
    Click Element   xpath:/html/body/nav/ul/li[2]/a
    Wait Until Page Contains       Log In

Enter Username
    [Arguments]     ${input}
    Input Text      id:username  ${input}

Enter Password
    [Arguments]     ${input}
    Input Text      id:password  ${input}

Enter First name
    [Arguments]     ${input}
    Input Text      id:firstname  ${input}

Enter Family name
    [Arguments]     ${input}
    Input Text      id:lastname  ${input}

Enter Phone number
    [Arguments]     ${input}
    Input Text      id:phone  ${input}

Click on Register button
    Submit Form
    Wait Until Page Contains    Log In

The Login page should be opened
    Page Should Contain     Demo app
    Page Should Contain Element     id:username
    Page Should Contain Element     id:password
    Page should Contain Element     xpath:/html/body/section/form/input[3]

Click on Log In button
    Submit Form
    Wait Until Page Contains      User Information
    Page Should Contain     Username
    Page Should Contain     First name
    Page Should Contain     Last name
    Page Should Contain     Phone number

The user information should be shown correctly on the main view
    Element Should Contain  id:username  ${username}
    Element Should Contain  id:firstname  ${firstname}
    Element Should Contain  id:lastname   ${familyname}
    Element Should Contain  id:phone  ${phonenumber}


