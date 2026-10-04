*** Settings ***
Library    BuiltIn

*** Variables ***
${Name}    Gagan

*** Test Cases ***
Print Variable
    Log To Console    My name is ${Name}