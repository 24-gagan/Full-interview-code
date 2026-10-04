*** Settings ***
Library    BuiltIn

*** Variables ***
${num}    100
${strg}    python
@{list_var}    java    python    oops    pytest
&{dict_var}    name=python    class_no=23    oops=True

*** Keywords ***
Keyword to print statement
    Log To Console    this is the message from keyword section

Keyword to get the argument
    [Arguments]    ${param1}
    Log To Console    this is printed in keyword section ${param1}

Keyword to return arguments
    ${num2}    Set Variable    200
    Log To Console    this is getting printed in keyword section ${num2}
    RETURN    ${num2}

Keyword to get and returned keyword
    [Arguments]    ${param1}    ${param2}
    ${added_val}    Evaluate    ${param1}+${param2}
    RETURN    ${added_val}

*** Test Cases ***
TC1 creating keyword
    Keyword to print statement

TC2 passing argument
    Keyword to get the argument    ${num}

TC3 returned arguments
    ${returned_val}    Keyword to return arguments
    Log To Console    this is printed in test case section ${returned_val}

TC4 Add two numbers
    ${value}    Keyword to get and returned keyword    10    20
    Log To Console    ${value}