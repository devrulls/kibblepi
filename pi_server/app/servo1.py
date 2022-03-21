import RPi.GPIO as GPIO
import time

PWM_GPIO = 18
FREQUENCE = 50

GPIO.setmode(GPIO.BCM)

#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


GPIO.setmode(GPIO.BCM) #Use BCM numerotation mode
GPIO.setwarnings(False) #Disable warnings

#Use pin 12 for PWM signal

GPIO.setup(PWM_GPIO, GPIO.OUT)
pwm = GPIO.PWM(PWM_GPIO, FREQUENCE)

#Init at 0°
pwm.start(angle_to_percent(0))
time.sleep(1)

#Go at 90°
pwm.ChangeDutyCycle(angle_to_percent(90))
time.sleep(1)

#Finish at 180°
pwm.ChangeDutyCycle(angle_to_percent(180))
time.sleep(1)

#Close GPIO & cleanup
pwm.stop()
GPIO.cleanup()