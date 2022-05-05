from pi_server import app
import RPi.GPIO as GPIO
import time
from pi_server.domain.convert_angle import convert_angle_to_servo_rotation

BUTTON_PIN = 26
PWM_GPIO = 18
FREQUENCE = 50
    

@app.route("/")
def index():
    return "Hello from Raspberry PI routes.py files"

@app.route("/push-button")
def check_push_button_state():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN)
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        servo()
        return "Button is pressed"
    return "Button is not pressed"


@app.route("/rotate-servo")
def servo():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PWM_GPIO, GPIO.OUT)
    pwm = GPIO.PWM(PWM_GPIO, FREQUENCE)
    GPIO.setwarnings(False) #Disable warnings

    #Init at 0°
    pwm.start(convert_angle_to_servo_rotation(0))
    time.sleep(1)

    #Go at 90°
    pwm.ChangeDutyCycle(convert_angle_to_servo_rotation(90))
    time.sleep(1)

    #Finish at 180°
    pwm.ChangeDutyCycle(convert_angle_to_servo_rotation(180))
    time.sleep(1)

    #Close GPIO & cleanup
    pwm.stop()
    GPIO.cleanup()
    return "rotate Servo routes.py :p"