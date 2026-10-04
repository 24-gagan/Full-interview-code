*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Click Example
    Open Browser    https://www.wikipedia.org    chrome
    Click Element    xpath=//*[@id="js-link-box-en"]
    Sleep    2s
    Close Browser