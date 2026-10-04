*** Settings ***
SSH Library

*** Variables ***
$Host 192.168.0.1
$Username admin
$Password 12345

Test case
[Documentation] Camera streaming should on
Open Connection $Hostname
Login $Username $Password
Open app lokito
Write 1
Output cat ls
Should contain output
