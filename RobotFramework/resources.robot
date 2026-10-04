*** Settings ***
Library    BuiltIn


*** Keywords ***
TC1 Print the keyword
    Log To Console    This is first keyword

Keyword to get arguments
    [Arguments]    ${param1}
    Log To Console    this is getting printed ${param1}

Keyword to return the arguments
    ${num2} =    Set Variable    200
    Log To Console    this is getting printed in keyword section ${num2}
    [Return]    ${num2}

Keword to get and return keyword
    [Arguments]    ${param1}    ${param2}
    ${added_val}    Evaluate    ${param1}+${param2}
    RETURN    ${added_val}