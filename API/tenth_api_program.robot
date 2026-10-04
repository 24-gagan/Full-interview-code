*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Test Cases ***
Update POSTS
    Create Session    api    https://jsonplaceholder.typicode.com
    ${data}=    Create Dictionary    id=1    title=Updated
    ${response}=    PUT On Session    api    /posts/1    json=${data}
    Should Be Equal As Integers    ${response.status_code}    200
    Log    ${response.json()}
    
