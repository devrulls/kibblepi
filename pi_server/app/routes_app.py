from app import app
# from app import helpers
# import RPi.GPIO as GPIO
import yagmail
import time

# BUTTON_PIN = 26
# LED_PIN_LIST = [17, 27, 22]
# PWM_GPIO = 18
# FREQUENCE = 50
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(BUTTON_PIN, GPIO.IN)
# GPIO.setup(PWM_GPIO, GPIO.OUT)
# pwm = GPIO.PWM(PWM_GPIO, FREQUENCE)
#
# for pin in LED_PIN_LIST:
#     GPIO.setup(pin, GPIO.OUT)
#
#
# for pin in LED_PIN_LIST:
#     GPIO.output(pin, GPIO.LOW)

@app.route("/")
def index():
    return "Hello from Raspberry PI "


@app.route("/send-email")
def send_email():
    password = ""
    with open("/home/pi/.local/share/.email_password", "r") as f:
        password = f.read()

    yag = yagmail.SMTP('test.devrulls@gmail.com', password)

    yag.send(to='rjhb85@gmail.com',
             subject="Email Test from Raspberry Pi",
             contents="Hello from Raspberry Pi"
             )

    return 'Email sent from test.devrulls@gmail.com!!!'


# @app.route("/push-button")
# def check_push_button_state():
#     if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
#         return "Button is pressed"
#     return "Button is not pressed"


# angle_to_percent = helpers.angle_percent.angle_to_percent()

#
# @app.route("/servo-kibblepi")
# def servo():
#     GPIO.setwarnings(False)  # Disable warnings
#
#     # Init at 0°
#     pwm.start(angle_to_percent(0))
#     time.sleep(1)
#
#     # Go at 90°
#     pwm.ChangeDutyCycle(angle_to_percent(90))
#     time.sleep(1)
#
#     # Finish at 180°
#     pwm.ChangeDutyCycle(angle_to_percent(180))
#     time.sleep(1)
#
#     # Close GPIO & cleanup
#     pwm.stop()
#     GPIO.cleanup()
#     return redirect("https://kibblepi.herokuapp.com", code=302)
