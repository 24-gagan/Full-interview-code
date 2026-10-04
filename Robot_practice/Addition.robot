*** Settings ***
Library    BuiltIn

*** Test Cases ***
Addition
    ${result}=    Evaluate    2+9
    Log To Console   Result is ${result}