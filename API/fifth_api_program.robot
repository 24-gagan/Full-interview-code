*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Delete Post
    Create Session    api    https://jsonplaceholder.typicode.com

    ${response}=    DELETE On Session
    ...    api
    ...    /posts/1

    Should Be Equal As Integers    ${response.status_code}    200