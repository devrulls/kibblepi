from app import app
from flask import redirect
import yagmail
import RPi.GPIO as GPIO
import time

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


@app.route("/")
def index():
    return "Hello from Raspberry PI "


@app.route("/send-email")
def send_email():
    password = ""
    with open("/home/pi/.local/share/.email_password", "r") as f:
        password = f.read()

    yag = yagmail.SMTP('test.devrulls@gmail.com', password)

    yag.send(to='@gmail.com',
             subject="Email Test from Raspberry Pi",
             contents="Hello from Raspberry Pi"
             )

    return 'Email sent from test.devrulls@gmail.com!!!'


@app.route("/push-button")
def check_push_button_state():
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        return "Button is pressed"
    return "Button is not pressed"


@app.route("/led/<int:led_pin>/state/<int:led_state>")
def trigger_led(led_pin, led_state):
    if not led_pin in LED_PIN_LIST:
        return "Wrong GPIO number: " + str(led_pin)
    if led_state == 0:
        GPIO.output(led_pin, GPIO.LOW)
    elif led_state == 1:
        GPIO.output(led_pin, GPIO.HIGH)
    else:
        return "State must be 0 or 1"
    return "OK"


# Set function to calculate percent from angle
def angle_to_percent(angle):
    if angle > 180 or angle < 0:
        return False

    start = 4
    end = 12.5
    ratio = (end - start) / 180  # Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


@app.route("/servo-kibblepi")
def servo():
    GPIO.setwarnings(False)  # Disable warnings

    # Init at 0°
    pwm.start(angle_to_percent(0))
    time.sleep(1)

    # Go at 90°
    pwm.ChangeDutyCycle(angle_to_percent(90))
    time.sleep(1)

    # Finish at 180°
    pwm.ChangeDutyCycle(angle_to_percent(180))
    time.sleep(1)

    # Close GPIO & cleanup
    pwm.stop()
    GPIO.cleanup()
    return redirect("https://kibblepi.herokuapp.com", code=302)


app.run(host="0.0.0.0", port=8080)
