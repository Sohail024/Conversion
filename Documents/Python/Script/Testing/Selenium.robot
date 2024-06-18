*** Settings ***
Library    SeleniumLibrary

*** Keywords ***

Start TestCase
    Open Browser    https://www.ebay.com    chrome
    Maximize Browser Window

Finish TestCase
    Close Browser
