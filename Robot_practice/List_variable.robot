*** Settings ***
Library    BuiltIn


*** Variables ***
@{list}    Python    java    Robot




*** Test Cases ***
Print List
    Log To Console    First Language : ${list[0]}
    Log To Console    First Language : ${list[1]}
    Log To Console    First Language : ${list[2]}