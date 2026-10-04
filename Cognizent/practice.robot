*** Settings ***
Library    BuiltIn
Library    Collections

*** Variables ***
${scalar}    10
@{list}    10    20    30
&{dict}    name=Gagan    Age=29

*** Test Cases ***
For loop
    FOR     ${num}    IN    @{list}
        Log To Console    ${num}
    END