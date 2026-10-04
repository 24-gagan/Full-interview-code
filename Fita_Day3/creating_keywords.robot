*** Settings ***
Library   BuiltIn
Resource    ./resources.robot

*** Variables ***
## scalar(numbers, sting), list, dict
${num1} =   100
${srtg} =   python
@{list_var} =   python   java   oops    pytest
&{dict_var} =   name=python   class_no=23   oops=True



*** Test Cases ***
TC1 creating Keyword
    Keyword to print the statement

TC2 passing arguments
    keyword to get the arguments   ${num1}

TC3 return arguments
    ${returned_val} =   keyword to return the arguments
    Log to Console   this is printed in the test case section ${returned_val}

TC4 Add two numbers
    ${value} =   keyword to get and return keyword   10   20
    Log to console   ${value}