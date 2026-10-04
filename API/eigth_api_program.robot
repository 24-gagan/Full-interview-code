*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Verify status code
    Create Session    api    https://jsonplaceholder.typicode.com
    ${response}=    GET On Session    api    /posts/1
    Should Be Equal As Integers    ${response.status_code}    200