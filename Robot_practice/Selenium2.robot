*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Get Title
    Open Browser    https://www.wikipedia.org    chrome
    ${title}    Get Title
    Log To Console    ${title}
    Close Browser