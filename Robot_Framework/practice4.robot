*** Settings ***
Library         SeleniumLibrary
Suite Setup     Open Browser to Google
Suite Teardown  Exit Application

*** Variables ***
${URL}      https://www.google.com
${Browser}  chrome

*** Keywords ***
Open browser to google
     Open Browser    ${URL}  ${Browser}
     Maximise Browser Window
     Set Selenium Implicit Wait    10s

*** Test Cases ***
Search in Google
    Input Text  name=q  Robot Framework
    Press Keys  name=q  Enter
    Wait untill page contains Robot Framework
    Page should contain Robot Framework