*** Settings ***
Library    SeleniumLibrary
Test Teardown    Capture Page Screenshot

*** Test Cases ***
Fail Example
    Open Browser    https://google.com    chrome
    Page Should Contain    InvalidText
    Close Browser