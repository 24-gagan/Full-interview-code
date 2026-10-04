*** Settings ***
Library    ../libraries/adb_library.py

*** Keywords ***
Connect ECU Device
    Connect Device

Launch Android Auto
    Launch Android Auto

Tap Maps Icon
    Tap Screen    600    400

Play Media
    Play Pause Media

Capture Logs
    Get Logs

Take Screenshot
    Take Screenshot