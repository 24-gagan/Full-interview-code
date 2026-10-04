*** Settings ***
Library   BuiltIn
Resource    ./resources.robot
Library   ./rf_function.py

Library   ./calc.py
Library   calc

*** Variables ***
## scalar(numbers, sting), list, dict
${num1} =   100
${srtg} =   python
@{list_var} =   python   java   oops    pytest
&{dict_var} =   name=python   class_no=23   oops=True

*** Test cases***
TC1: Call rf python library- fucntion
    ${added_val} =   add_two_numbers   10   20
    Log to console   ${added_val}

TC2: Call rf python library - class
    ${added_val} =   calc.add   10   20
    Log to console   ${added_val}

TC3: Call rf python library- fucntion
    ${n1} =   Convert To Integer   10
    ${n2} =   Convert To Integer   20
    ${added_val} =   add_two_numbers   ${n1}   ${n2}
    Log to console   ${added_val}