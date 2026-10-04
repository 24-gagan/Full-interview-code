*** Settings ***
Library    SSHLibrary
Suite Setup    SSH Open Connection
Suite Teardown    Close Connection

*** Variables ***
${HOST}       192.168.0.1
${USERNAME}   admin
${PASSWORD}   password123

*** Keywords ***
SSH Open Connection
    Open Connection    ${HOST}
    Login    ${USERNAME}    ${PASSWORD}

*** Test Cases ***
Search the string
    ${output}=    Execute Command    ls | grep Home
    Should Contain    ${output}    Home
    Log To Console    ${output}
    Log    Pass