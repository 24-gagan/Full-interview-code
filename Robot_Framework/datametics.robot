*** Settings ***
Library           SSHLibrary
Suite Setup       Open Connection And Login
Suite teardown    Close All Connections


*** Variables ***
@{dict1} Usrename=admin  Password=123   HOST=192.168.0.1

*** Test Cases ***
Execute Dictinary Values