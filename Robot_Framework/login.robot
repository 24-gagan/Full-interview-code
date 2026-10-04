*** Settings ***
Library    SSHLibrary
Suite Setup    Open Connection    ${HOST}    port=${PORT}
Suite Teardown    Close Connection

*** Variables ***
${HOST} 192.168.0.1
${USERNAME} admin
${PASSWORD} password123
${PORT} 115200
*** Keywords ***
Open Connection and Login
    Open Connection    ${HOST}    port=${PORT}
    Login    ${USERNAME}    ${PASSWORD}

*** Test Cases ***
Execute home directry List
    Open Connection and Login
    Execute Command    ls -l /home
    Login to Console