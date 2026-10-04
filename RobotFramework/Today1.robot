*** Settings ***
Library    BuiltIn

*** Variables ***
${str1} =    21
${str2} =    21
@{list2}=    python    oops    java    c++
*** Test Cases ***
Addition of two numbers
    ${sum} =    Evaluate    ${str1} + ${str2}
    Log To Console    ${sum}
    
Greater number
    IF    ${str1} > ${str2}
        Log To Console    ${str1} is greater
    ELSE
        Log To Console    ${str2} is greater
    END
   
Equal number
    IF    ${str1} == ${str2}
        Log To Console    ${str1} and ${str2} is equal
    ELSE
        Log To Console    Should Not Be Equal
    END

Iterating in list
    FOR    ${var2}    IN    @{list2}
        Log To Console    ${var2}
    END

Access List ELements
    Log To Console    First Element : ${list2}[0]
    Log To Console    Second Element : ${list2}[1]