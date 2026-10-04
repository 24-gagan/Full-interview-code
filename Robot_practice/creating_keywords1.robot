*** Settings ***
Library    BuiltIn
Resource    ./resource.robot
*** Variables ***
# Scalar List Dictionary
${num}    100
${srtg}   python
@{list_var}    java    python    oops    pytest
&{dict_var}    name=python    class_no=23    oops=True



*** Test Cases ***
TC1 creating keyword
    Keyword to print the statement

TC2 passing arguments
    Keyword to get the arguments    ${num}

TC3 return arguments
    ${returned_val}    Keyword to return arguments
    Log To Console    this is printed the test case section ${returned_val}

TC4 Add two numbers
    ${value}    Keyword to add two numbers    10    20
    Log To Console    ${value}