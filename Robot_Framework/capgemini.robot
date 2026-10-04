*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser To Login Page
Suite Teardown    Close Browser

*** Variables ***
${URL}      https://google.com
${BROWSER}  Chrome

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    0.5s
    Set Selenium Implicit Wait    5s
    Go To    ${URL}
    Wait Until Page Contains Element    name=q
    Input Text    name=q    Robot Framework
    Press Keys    name=q    ENTER
    Wait Until Page Contains    Robot Framework - Google Search

*** Test Cases ***
Search for Robot Framework
    [Documentation]    This test case searches for Robot Framework on Google and verifies the results.
    Open Browser To Login Page
    Wait Until Page Contains    Robot Framework - Google Search
    Log To Console    Search for Robot Framework test case executed successfully.
    Log To Console    Demonstrates using SeleniumLibrary to automate a web search.