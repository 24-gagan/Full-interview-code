*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Verify Username
    Create Session    api    https://jsonplaceholder.typicode.com
    ${response}=    GET On Session    api    /users/1
    ${json}=    Set Variable    ${response.json()}
    Should Be Equal    ${json}[username]    Bret