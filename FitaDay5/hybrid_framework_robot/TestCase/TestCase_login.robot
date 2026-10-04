
*** Settings ***
Library         SeleniumLibrary
Variables       ../TestData/data.py
variables       ../TestData/xpath.py
Resource        ../Resource/keyword.robot
Test Setup      Login to application
Test Teardown   Close Browser

*** Test Cases ***
Login to demo website and verify title
#    Set Log Level   Trace
#    Open Browser   https://www.saucedemo.com/   chrome
    Title Should Be   Swag Labs
#    Close Browser

Login to the application using username and password
    [tags]   sanity
#    Set Log Level   Trace
#    Open Browser   https://www.saucedemo.com/   chrome
    Input Text   ${id_input_username}   ${username}
    Input Password    ${name_input_password}  ${password}
    Click Button   ${xpath_button_login}
    ${logo_text} =    Get Text   ${class_text_logo}
    Run Keyword If   '${logo_text}'=='Swag Labs'   Log to Console   Test Passed   ELSE   FAIL   logo text is incorrect
#    Close Browser

Logout and verify the application
    [tags]   TC3    sanity   regression
#    Set Log Level   Trace
#    Open Browser   https://www.saucedemo.com/   chrome
    Input Text   ${id_input_username}   ${username}
    Input Password    ${name_input_password}   ${password}
    Click Button   ${xpath_button_login}
    Click Button   ${id_button_menu}
    Wait Until Element Is Visible   ${id_link_logout}    ${timeout}
    Click Link   ${id_link_logout}
    Element Should Be Visible    ${xpath_button_login}
#    Close Browser
