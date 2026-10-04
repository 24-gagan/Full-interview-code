*** Settings ***
Library    BuiltIn

*** Variables ***
${result}=    Evaluate 2+3
*** Test Cases ***
Addition of number
    Log To Console    ${result}