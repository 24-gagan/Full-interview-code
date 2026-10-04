*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Get Text
    Open Browser    https://example.com    chrome
    ${text}    Get Text    xpath=//h1
    Log To Console    ${text}
    Close Browser