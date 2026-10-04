*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Test Cases ***
Create New Post
    Create Session    api    https://jsonplaceholder.typicode.com

    ${body}=    Create Dictionary
    ...    title=Robot Framework
    ...    body=API Testing
    ...    userId=1

    ${response}=    POST On Session
    ...    api
    ...    /posts
    ...    json=${body}

    Should Be Equal As Integers
    ...    ${response.status_code}
    ...    201

    Log    ${response.json()}