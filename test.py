import RPi.GPIO as GPIO
import time

BUZZER_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN,2000)
pwm.start(50)
time.sleep(1)
pwm.stop()

GPIO.cleanup()
