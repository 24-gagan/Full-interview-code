*** Settings ***
Library    SSHLibrary
Suite Setup    Open SSH Connection
Suite Teardown    Close Connection

*** Variables ***
${HOST} 192.168.0.1
${USERNAME} admin
${PASSWORD} password123

*** Keywords ***
Open ECU Connection
    Open Connection  ${HOST}  timeout=30s
    Login  ${USERNAME}  ${PASSWORD}

*** Test Cases ***
Write to ECU
    ${output}=  Execute Command echo "Hello, ECU!"
    Log  ${output}