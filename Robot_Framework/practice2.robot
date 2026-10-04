*** Settings ***
Library    SSHLibrary
Suite Setup    Open Connection and Login
Suite Teardown    Close All Connections

*** Variables ***
${Host}        192.168.0.1
${Username}    admin
${Password}    password123

*** Keywords ***
Open Connection and Login
    Open Connection    ${Host}    timeout=30s
    Login    ${Username}    ${Password}

*** Test Cases ***
Linux command execution
    ${output}=    Execute Command    dmesg | grep usb
    Log To Console    ${output}
    Should Contain    ${output}    usb
    Log To Console    PASS
