import RPi.GPIO as GPIO
import time

def open():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(4,GPIO.OUT)

	p = GPIO.PWM(4,50)
	p.start(7.5)

	p.ChangeDutyCycle(12.5)
	time.sleep(1)

	p.stop()
	GPIO.cleanup()


def halfClose():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(4,GPIO.OUT)

	p = GPIO.PWM(4,50)
	p.start(7.5)

	p.ChangeDutyCycle(8.5)
	time.sleep(1)

	p.stop()
	GPIO.cleanup()


def close():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(4,GPIO.OUT)

	p = GPIO.PWM(4,50)
	p.start(7.5)

	p.ChangeDutyCycle(7.0)
	time.sleep(1)

	p.stop()
	GPIO.cleanup()
