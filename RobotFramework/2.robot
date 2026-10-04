*** Settings ***
Library    BuiltIn

*** Variables ***
${num1} =     100
${strg} =    python
@{list_var} =    python    java    oops    pytest
&{dict_var} =    name=python     class_no=23     oops=True

*** Test Cases ***

TC1 Print the statement
    Log To Console    This is the stateement

TC2 printing variables
    Log To Console    Scaler number ${num1}
    Log To Console    Scaler string ${strg}
    Log To Console    List @{list_var}
    Log To Console    Dict &{dict_var}