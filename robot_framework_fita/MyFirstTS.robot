*** Settings ***
Library  BuiltIn

*** Variables ***
# scalar(numbers , string), list, dict
${num1}        100
${strg}        python
@{list_var}    python    java    oops    pytest
&{dict_var}    name=python    class_no=23    oops=True


*** Test Cases ***
TC1 Print the statement
    Set Log Level    TRACE
    Log    This is the message    console=True    level=TRACE

TC2 Printing variables
    Log    Scalar number ${num1}    console=True
    Log    Scalar string ${strg}    console=True
    Log    List @{list_var}         console=True
    Log    Dictionary ${dict_var}   console=True

TC3 accessing list
    Log    List first element ${list_var}[0]    console=True
    FOR    ${var}    IN    @{list_var}
        Log To Console    ${var}
    END

TC3 accessing dictionary
    Log    dict element ${dict_var['name']}    console=True
    FOR    ${var}    IN    &{dict_var}
        Log To Console    ${var}
    END