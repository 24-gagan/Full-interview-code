*** Settings ***
Library   BuiltIn

*** Variables ***
## scalar(numbers, sting), list, dict
${num1} =   100
${srtg} =   python
@{list_var} =   python   java   oops    pytest
&{dict_var} =   name=python   class_no=23   oops=True


*** Test Cases ***

TC1 Print the statement
    Set Log Level   TRACE
    Log   This is the message   console=True   level=TRACE

TC2 printing variables
    Log   Scalar number ${num1}    console=True
    Log   Scalar string ${srtg}    console=True
    Log   list @{list_var}    console=True
    Log   dictionary &{dict_var}    console=True

TC3 accessing list
    Log   list first element ${list_var[0]}    console=True
    FOR    ${var}   IN   @{list_var}
        Log to console   ${var}
    END

TC4 accessing Dictonary
    Log   dict element ${dict_var['name']}    console=True
    FOR    ${var}   IN   &{dict_var}
        Log to console   ${var[0]} :: ${var[1]}
    END