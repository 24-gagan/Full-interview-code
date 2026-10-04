*** Settings ***
Library    BuiltIn

*** Variables ***
# Scalar List Dictionary
${num}    100
${srtg}   python
@{list_var}    java    python    oops    pytest
&{dict_var}    name=python    class_no=23    oops=True

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

Keyword to get and return keyword
    [Arguments]    ${param1}    ${param2}
    ${added_val}    =    Evaluate    ${param1}+${param2}
    RETURN

*** Test Cases ***
TC1 creating keyword
    Keyword to print the statement

TC2 passing arguments
    Keyword to get the arguments    ${num}

TC3 return arguments
    ${returned_val}    Keyword to return arguments
    Log To Console    this is printed the test case section ${returned_val}

TC4 Add two numbers
...   ${value}