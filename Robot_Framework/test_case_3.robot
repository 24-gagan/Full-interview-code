*** Settings ***
Library    SSHLibrary
Suite Setup    Open SSH Connection
Suite Teardown    Close Connection

*** Variables ***
${HOST}      192.168.1.10
${USERNAME}  admin
${PASSWORD}  password123

*** Keywords ***
Open SSH Connection
    Open Connection    ${HOST}    timeout=30s
    Login    ${USERNAME}    ${PASSWORD}

Validate Logged In User
    ${user}=    Execute Command    whoami
    Should Be Equal    ${user.strip()}    ${USERNAME}
