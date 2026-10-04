*** Settings ***
Library           AppiumLibrary
Resource          ../resources/variables.robot
Suite Setup       Open My Application
Suite Teardown    Close Application
Test Teardown     Capture Page Screenshot

*** Keywords ***
Open My Application
    Open Application
    ...    ${REMOTE_URL}
    ...    platformName=${PLATFORM_NAME}
    ...    platformVersion=${PLATFORM_VERSION}
    ...    deviceName=${DEVICE_NAME}
    ...    automationName=${AUTOMATION_NAME}
    ...    app=${APP_PATH}

Click On Element By Text
    [Arguments]    ${text}
    Click Element    xpath=//*[@text="${text}"]

Input Text By Resource Id
    [Arguments]    ${id}    ${value}
    Input Text    id=${id}    ${value}

Scroll Down
    Swipe    500    1500    500    500    800

Press Android Back Button
    Press Keycode    4

Wait And Verify Text
    [Arguments]    ${text}
    Wait Until Page Contains    ${text}    10s

*** Test Cases ***
Verify App Launch Successfully
    Wait Until Page Contains Element    xpath=//*    10s

Navigate To Forms Screen
    Click On Element By Text    Forms
    Wait And Verify Text    Form components

Enter And Validate Input Field
    Click On Element By Text    Forms
    Input Text By Resource Id    com.wdiodemoapp:id/input-text    Automation Test
    Page Should Contain Text    Automation Test

Verify Switch Toggle
    Click On Element By Text    Forms
    Click Element    id=com.wdiodemoapp:id/switch
    Element Should Be Visible    id=com.wdiodemoapp:id/switch

Scroll And Verify Element
    Click On Element By Text    Swipe
    Scroll Down
    Wait Until Page Contains Element    xpath=//*[@text="You found me!!!"]    10s

Verify Back Navigation
    Click On Element By Text    Forms
    Press Android Back Button
    Wait Until Page Contains Element    xpath=//*[@text="Home"]    10s
