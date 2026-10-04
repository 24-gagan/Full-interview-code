***setting***
Library Selenium

***variables***
$Hostname  192.168.0.1
$Username  Gagan
$Password   12345

***Test Case***
Login to amazon site and try to signup
Host   Hostname
Login   Username    Password
$output cd /l
Should contain  output
