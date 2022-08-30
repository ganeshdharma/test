*** Settings ***
Library  Tolerence.py


*** Test Cases ***
test1
    ${output}=  hello  a
    Should be equal as integers  ${output}  14
*** Keywords ***
hello
    [Arguments]  ${var}
    ${output}=  RAN  a
    [Return]  ${output}



