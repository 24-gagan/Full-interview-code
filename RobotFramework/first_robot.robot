*** Settings ***
Library    BuiltIn
Resource    ./variables.robot
Resource    ./keywords.robot
Test Setup    Start Test
Test Teardown    End Test

*** Test Cases ***
First program
    Log To Console    Gagan
Second program
    Log To Console    ${name}
Third Program 
    ${value}=    Evaluate    ${a} + ${b}
    Log To Console    ${value}
Using keyword one
    Forth Program
Using keyword two
    Fifth Program
Sixth Program hone wala hai
    Sixth program doing    10    20
Seventh program hone wala hai
    Seventh program doing    3    6