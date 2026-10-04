*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
Search Example
    Open Browser    https://www.google.com chrome
    Input Text   name=q    Robot Framework
    Sleep 2s
    Close Browser