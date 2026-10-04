*** Settings ***
Library    BuiltIn

*** Variables ***
${num}   10

*** Test Cases ***
If condition
    IF    ${num}>5
         Log To Console    Number is greater than 5
    ELSE
        Log To Console    Number is not greater than 5
    END
