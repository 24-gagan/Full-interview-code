*** Settings ***
Library    BuiltIn
Resource    ./resource.robot
Library    ./rf_function.py
Library    ./calc.py
Library    calc
*** Variables ***
# Scalar List Dictionary
${num}    100
${srtg}   python
@{list_var}    java    python    oops    pytest
&{dict_var}    name=python    class_no=23    oops=True

*** Test Cases ***
TC1: Call rf python library
    ${added_val}     add_two_numbers    10    20
    Log To Console    ${added_val}}

TC2: Call rf python library - class
    ${added_val}    calc.add    10    20
    Log To Console    ${added_val}