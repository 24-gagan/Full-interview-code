***Setting***
Library SSH Library

***Variable***
${HOST}  192.168.0.1
${USERNAME} root
${PASSWORD} 12345

***Keyword***
Open connection and login
        Open Connection   ${HOST}
        Login   ${USERNAME} ${PASSWORD}

***Test case***
SSH Connect list through ssh
        ${output}   Execute Command ls -l /home
        Login to Console ${output}
