from messenger import Messenger
from gpiozero import LED
from gpiozero import MotionSensor

messenger = Messenger()

green_led = LED(17)
motion_sensor = MotionSensor(4)

while True:
    motion_sensor.wait_for_active()
    messenger.send_motion_alert()
    green_led.on()
    motion_sensor.wait_for_inactive()
    green_led.off()
