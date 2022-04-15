import time

import RPi.GPIO as GPIO
from werkzeug.utils import redirect

from pi_server import app
from pi_server.domain.convert_angle import convert_angle_to_servo_rotation

BUTTON_PIN = 26
LED_PIN_LIST = [17, 27, 22]
PWM_GPIO = 18
FREQUENCE = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(PWM_GPIO, GPIO.OUT)
pwm = GPIO.PWM(PWM_GPIO, FREQUENCE)

for pin in LED_PIN_LIST:
    GPIO.setup(pin, GPIO.OUT)

for pin in LED_PIN_LIST:
    GPIO.output(pin, GPIO.LOW)


@app.route("/rotate-servo")
def servo():
    pwm.start(convert_angle_to_servo_rotation(0))
    time.sleep(1)

    pwm.ChangeDutyCycle(convert_angle_to_servo_rotation(90))
    time.sleep(1)

    pwm.ChangeDutyCycle(convert_angle_to_servo_rotation(180))
    time.sleep(1)

    pwm.stop()
    GPIO.cleanup()
    return redirect("https://kibblepi.herokuapp.com", code=302)
