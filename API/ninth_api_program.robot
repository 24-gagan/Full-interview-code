*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Test Cases ***
Create Post
    Create Session    api    https://jsonplaceholder.typicode.com
    ${data}=    Create Dictionary    title=Robot    body=API Test    userID=1
    ${response}=    POST On Session    api    /posts    json=${data}
    Log    ${response.json()}