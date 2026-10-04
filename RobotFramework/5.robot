*** Test Cases ***
Even Odd Check
    ${num}=    Set Variable    10

    IF    ${num} % 2 == 0
        Log To Console    Even Number
    ELSE
        Log To Console    Odd Number
    END
``