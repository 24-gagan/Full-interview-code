*** Settings ***
Library    BuiltIn

*** Variables ***
${num1}       100
${strg}       python
@{list_var}   python    java    oops    pytest
&{dict_var}   name=python    class_no=23    oops=True

*** Test Cases ***
TC 1 Print The Statement
    Log    This is the message    console=True

TC 2 Printing Variables
    Log    Scalar number ${num1}    console=True
    Log    String ${strg}    console=True
    Log    List ${list_var}    console=True
    Log    Dictionary ${dict_var}    console=True

TC 3 Accessing List
    Log    List first element ${list_var}[0]    console=True

    FOR    ${var}    IN    @{list_var}
        Log To Console    ${var}
    END