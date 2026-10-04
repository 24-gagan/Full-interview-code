*** Settings ***
Library    RequestsLibrary


*** Test Cases ***
Delete posts
    Create Session    api    https://jsonplaceholder.typicode.com
    ${response}=    DELETE On Session    api     /posts/1
    Log    ${response.status_code}

