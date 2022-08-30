*** Settings ***
Library   fridge.py

Test Setup      Connect
Test Teardown   Disconnect

*** Test Cases ***
the temperature setpoint of the fridge1
    change_temperature_setpoint  4
    check_temperature_setpoint   6
the temperature setpoint of the fridge2

    change temperature setpoint  8
    Check temperature setpoint   8
the temperature setpoint of the fridge3

    Change_Temperature SETPOINT  3.5
    CHECK temperature_SETpoint   3.5