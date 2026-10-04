*** Variables ***
&{USER}    name=Gagan    age=28

*** Test Cases ***
Dictionary example
    Log To Console    Name: ${USER}[name]