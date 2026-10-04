*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Browser Example
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window
    Sleep    3s
    Close Browser