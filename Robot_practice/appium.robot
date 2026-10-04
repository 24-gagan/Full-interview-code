*** Settings ***
Library    AppiumLibrary
Resource    ./resource1.robot
*** Variables ***
&{CAPS}
...    platformName=Android
...    deviceName=emulator-5554
...    appPackage=com.android.settings
...    appActivity=.Settings

*** Test Cases ***
Open Settings App
    Open Application    http://localhost:4723/wd/hub    &{CAPS}
    Wait Until Element Is Visible    id=android:id/list    10s
    Click Element    xpath=//android.widget.TextView[@text="Bluetooth"]
    Close Application