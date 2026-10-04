*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com

*** Test Cases ***
Get User Details
    Create Session    api    ${BASE_URL}

    ${response}=    GET On Session    api    /users/1

    Should Be Equal As Integers    ${response.status_code}    200

    ${json}=    Set Variable    ${response.json()}

    Should Be Equal As Integers    ${json}[id]    1

    Log    ${json}[id]