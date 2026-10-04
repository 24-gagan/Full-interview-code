
*** Settings ***
Library   BuiltIn

*** Keywords ***
Keyword to print the statement
    Log to console    this is the messge from keyword section

keyword to get the arguments
    [Arguments]   ${param1}
    log to console   this is getting printed in keywrd sec ${param1}

keyword to return the arguments
    ${num2} =   Set variable   200
    log to console   this is getting printed in keywrd sec ${num2}
    [return]   ${num2}

keyword to get and return keyword
    [Arguments]   ${param1}    ${param2}
    ${added_val} =   evaluate   ${param1}+${param2}
    [return]   ${added_val}