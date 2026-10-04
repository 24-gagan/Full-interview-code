*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Google And Verify Title
    Open Browser    https://www.google.com    chrome
    Title Should Be    Google
    [Teardown]    Close Browser
