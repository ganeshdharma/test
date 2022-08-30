import  robot.api.logger
import robot.utils.asserts

temperature_setpoint = 5
 

def ble_send_setpoint(value):
    global  temperature_setpoint
    temperature_setpoint = value
    print('Sending setpoint to the fridge: ', temperature_setpoint)


def ble_read_setpoint():
    global  temperature_setpoint
    print('Reading setpoint to the fridge: ', temperature_setpoint)
    return  temperature_setpoint


def change_temperature_setpoint(value):
    value = float(value)
    robot.api.logger.info('Change temperature setpoint to %f' % value)
    ble_send_setpoint(value)


def check_temperature_setpoint(expected):
    expected = float(expected)
    actual = ble_read_setpoint()
    robot.utils.asserts.assert_equal(expected, actual)

def connect():
    """Pretend to connect to the fridge."""
    robot.api.logger.info('Connect to the frige')


def disconnect():
    """Pretend to disconnect from the fridge."""
    robot.api.logger.info('Disconnect from the frige')

# a=ble_send_setpoint(4)
# print(a)
av=check_temperature_setpoint(8)
print(av)