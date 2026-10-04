
*** Keywords ***
Login to application
    Set Log Level   Trace
    Open Browser   ${url}   ${browser}
    Maximize Browser Window