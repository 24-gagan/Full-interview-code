*** Settings ***
Library    BuiltIn

*** Variables ***
${Name}    Gagan

*** Test Cases ***
Print the name
    Log To Console    ${Name}

Addition
    ${result}=    Evaluate    10+20
    Log To Console    Result= ${result}
Equal check
    Should Be Equal    Hello    Hello
String Check
    ${text}=    Set Variable    Robot Framework
    Should Contain    ${text}    Robot