*** Settings ***
Library    BuiltIn

*** Variables ***
@{List}    10    20    30   40


*** Test Cases ***
For loop
    FOR     ${num}    IN    @{List}
        Log To Console    Number : ${num}
    END