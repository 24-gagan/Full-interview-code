*** Settings ***
Library    BuiltIn


*** Keywords ***
Keyword to print the statement
    Log To Console    this is the message from keyword section

Keyword to get the arguments
    [Arguments]    ${param1}
    Log To Console    this is getting printed in keyword section ${param1}

Keyword to return arguments
    ${num2}    Set Variable    200
    Log To Console    this is getting printed in keyword sec ${num2}
    RETURN    ${num2}

Keyword to add two numbers
    [Arguments]    ${param1}    ${param2}
    ${added_val}    Evaluate    ${param1}+${param2}
    RETURN    ${added_val}