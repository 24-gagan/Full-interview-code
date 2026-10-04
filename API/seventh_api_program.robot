*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Get all posts
    Create Session    api    https://jsonplaceholder.typicode.com
    ${response}=    GET On Session    api    /posts
    Log    ${response.json()}
