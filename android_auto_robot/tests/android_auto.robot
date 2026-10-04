*** Settings ***
Resource    ../resources/adb_keywords.robot

*** Test Cases ***
Android Auto Projection Validation
    Connect ECU Device
    Launch Android Auto
    Sleep    5s

    Tap Maps Icon
    Sleep    3s

    Play Media
    Sleep    5s

    Take Screenshot
    Capture Logs