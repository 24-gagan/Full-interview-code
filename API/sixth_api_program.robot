*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Get user details
    Create Session    api    https://jsonplaceholder.typicode.com
    ${response}=    GET On Session    api    /users/1
    Should Be Equal As Integers    ${response.status_code}    200
    Log    ${response.json()}
