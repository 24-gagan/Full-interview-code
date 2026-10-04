*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Validate User Name
    Create Session    api     https://jsonplaceholder.typicode.com
    ${response}=    GET On Session    api    /users/1
    ${json}=    Evaluate    $response.json()
    Should Be Equal    ${json["name"]}    Leanne Graham
    
