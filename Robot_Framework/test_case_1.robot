*** Settings ***
Library    SSHLibrary
Suite Setup    Open Connection And Login
Suite Teardown    Close Connection

*** Variables ***
${HOST}      192.168.1.10
${USERNAME}  admin
${PASSWORD}  password123

*** Keywords ***
Open Connection And Login
    Open Connection    ${HOST}
    Login    ${USERNAME}    ${PASSWORD}

*** Test Cases ***
Execute Home Directory List
    ${output}=    Execute Command    ls -l /home
    Log To Console    ${output}
