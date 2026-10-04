*** Setting ***
Library SSHLibrary

*** Variables ***
${HOST} 192.168.0.1
${USERNAME} root
${PASSWORD} gagan

*** Keywords ***
Open Connection ${HOST}
Login   ${USERNAME} ${PASSWORD}

*** TestCase ***
SSH Command will give list through linux command
${output}   Execute Command ls-l/home
Login To Console    ${output}