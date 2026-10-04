*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Test Cases ***
Update Post
    Create Session    api    https://jsonplaceholder.typicode.com

    ${body}=    Create Dictionary
    ...    id=1
    ...    title=Updated Post

    ${response}=    PUT On Session
    ...    api
    ...    /posts/1
    ...    json=${body}

    Should Be Equal As Integers    ${response.status_code}    200