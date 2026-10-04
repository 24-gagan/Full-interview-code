*** Settings ***
Library    BuiltIn

*** Variables ***
# Scalar List Dictionary
${num}    100
${srtg}   python
@{list_var}    java    python    oops    pytest
&{dict_var}    name=python    class_no=23    oops=True

*** Test Cases ***
TC1 print the statement
    Set Log Level    TRACE
    Log    Gagandeep    console=True

TC2 printing variables
    Log    Scalar number: ${num}    console=True
    Log    Scalar string: ${srtg}    console=True
    Log    List: ${list_var}    console=True
    Log    Dictionary: ${dict_var}    console=True

TC3 access list
    Log To Console    List first element: ${list_var[0]}

    FOR    ${item}    IN    @{list_var}
        Log To Console    Programming Name : ${item}
    END

TC4 Print Dictionary Using Loop
    FOR    ${key}    IN    @{dict_var.keys()}
        Log To Console    ${key} : ${dict_var}[${key}]
    END