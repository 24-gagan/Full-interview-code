*** Settings ***
Library    BuiltIn
Library    ./rf_function.py
Resource    ./resource.robot
Library    ./calc.py

*** Variables ***
# Scalar List Dictionary
${num}    100
${srtg}   python
@{list_var}    java    python    oops    pytest
&{dict_var}    name=python    class_no=23    oops=True

*** Test Cases ***
TC1 Call rf library
    ${added_val}    Add Two Numbers    10    20
    Log To Console   ${added_val}

TC2 class
    ${added_val}    Add    10     30
    Log To Console    ${added_val}