# CanePal
# code modified from ultrasonic_dist_demo and
# servo_demo presented in INFO 697 at Pratt Institute
# with Dr. Maceli and Basem Ali

from microbit import *
from machine import time_pulse_us
from servo_lib import *
# import music for sound

# for ultrasonic module refer to documentation at:
# https://wiki.keyestudio.com/KS0361(KS0365)_keyestudio_37_in_1_Starter_Kit_for_BBC_micro:bit#Project_21:_Ultrasonic_Ranging
# for accelerometer documentation refer to:
# https://microbit-micropython.readthedocs.io/en/latest/accelerometer.html


# set pins for ultrasonic sensor
trig = pin2  # the trigger pulse signal is attached to pin2
echo = pin1  # this is the echo sensor
trig.write_digital(0)
echo.read_digital()

# Setting up servo to start at 0 degrees
Servo(pin0).write_angle(0)
sleep(1000)

# If an object is within 36in of the cane
#the cane will vibrate via the microservo
while True:
    # trigger pulse on/off
    trig.write_digital(1)
    trig.write_digital(0)
    # calculate the high level duration of the pulse
    microsec = time_pulse_us(echo, 1)
    time_echo = microsec / 1000000
    # calculate the test distance = (time for high level duration/2)
    # x (velocity of sound 340m/s=34300)
    dist_cm = (time_echo / 2) * 34300
    # convert distance into inches 1in = 2.54cm
    dist_inches = dist_cm/2.54
    # if the distance of the detected object is within 36in cane will vibrate
    if dist_inches <= 36:
        while True:
            # run vibration code
            Servo(pin0).write_angle(0)
            sleep(1000)
            Servo(pin0).write_angle(180)
            sleep(1000)
    else:
        continue
    sleep(300)
    # if the accelerometer reads the current gesture as 'freefall' play a sound
    # if accelerometer.is_gesture('freefall'):
    # display.scroll("FALL")
    # music.play(music.BADDY)
    # else:
    # continue
    sleep(1000)

