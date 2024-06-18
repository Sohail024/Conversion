*** Settings ***
Library    Browser

*** Keywords ***

Start TestCase
    New Browser browser=chromium
    New Page    https://www.ebay.com   
    Set Viewport Size width=1920 height=1080

Finish TestCase
    Close Browser
