*** Settings ***
Library    BuiltIn

*** Keywords ***
Print message
    Log To Console    This is custom keyword

*** Test Cases ***
Call keyword
    Print Message