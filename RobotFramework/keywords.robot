*** Settings ***
Library    BuiltIn

*** Keywords ***
Start Test
    Log To Console    Test Started
Forth Program
    FOR    ${i}    IN    @{list1}
        Log To Console    ${i}
    END
Fifth program
    FOR    ${i}    IN    &{Dict1}
        Log To Console    ${i}
    END
Sixth program doing
    [Arguments]    ${a}    ${b}
    ${sum}=    Evaluate    ${a} + ${b}
    Log To Console    ${sum}
Seventh program doing
    [Arguments]    ${c}    ${d}
    ${multiply}=  Evaluate    ${c} * ${d}
    [Return]    ${multiply}
End Test
    Log To Console    Test Ended