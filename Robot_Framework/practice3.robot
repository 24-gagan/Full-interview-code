*** Settings ***
Library           SeleniumLibrary
Suite Setup       Open Browser To Google
Suite Teardown    Close Browser

*** Variables ***
${URL}            https://www.google.com
${BROWSER}        chrome

*** Keywords ***
Open Browser To Google
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

*** Test Cases ***
Search In Google
    Input Text    name=q    Robot Framework
    Press Keys    name=q    ENTER
    Wait Until Page Contains    Robot Framework
    Page Should Contain    Robot Framework