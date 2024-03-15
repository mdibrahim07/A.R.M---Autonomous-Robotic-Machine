import RPi.GPIO as GPIO 
import time 

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM) 

# Define GPIO pins
TRIG = 17  # Ultrasonic sensor trigger pin
ECHO = 27  # Ultrasonic sensor echo pin
led = 26   # LED pin for indication

# Define motor pins
m1a = 23
m1b = 24
m2a = 25
m2b = 8

# Suppress warnings
GPIO.setwarnings(False) 

# Setup GPIO pins
GPIO.setup(TRIG, GPIO.OUT)  # Trigger pin as output
GPIO.setup(ECHO, GPIO.IN)    # Echo pin as input
GPIO.setup(led, GPIO.OUT)    # LED pin as output

# Setup motor control pins
GPIO.setup(m1a, GPIO.OUT)
GPIO.setup(m1b, GPIO.OUT)
GPIO.setup(m2a, GPIO.OUT)
GPIO.setup(m2b, GPIO.OUT)

# Set up PWM for motor control
pwm_m1a = GPIO.PWM(m1a, 100)  # PWM for motor 1A with 100 Hz frequency
pwm_m1b = GPIO.PWM(m1b, 100)  
pwm_m2a = GPIO.PWM(m2a, 100)
pwm_m2b = GPIO.PWM(m2b, 100)

# Start PWM with 0% duty cycle
pwm_m1a.start(0)
pwm_m1b.start(0)
pwm_m2a.start(0)
pwm_m2b.start(0)

print("running")

# Function to stop the motors
def stop():
    pwm_m1a.ChangeDutyCycle(0)
    pwm_m1b.ChangeDutyCycle(0)
    pwm_m2a.ChangeDutyCycle(0)
    pwm_m2b.ChangeDutyCycle(0)

# Function to move the robot forward
def forward():
    pwm_m1a.ChangeDutyCycle(100)  # Adjust duty cycle for desired speed 
    pwm_m1b.ChangeDutyCycle(0)
    pwm_m2a.ChangeDutyCycle(100)
    pwm_m2b.ChangeDutyCycle(0)

# Function to make the robot turn left
def left():
    pwm_m1a.ChangeDutyCycle(0)
    pwm_m1b.ChangeDutyCycle(0)
    pwm_m2a.ChangeDutyCycle(100)
    pwm_m2b.ChangeDutyCycle(0)

stop()
try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        pulse_start = time.time()
        pulse_end = time.time()
        
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        print(distance)

        # If an obstacle is detected within 15cm, turn left; otherwise, move forward
        if distance < 15:
            left()
            print("running left")
            time.sleep(1)
        else:
            forward()
            print("running forward")
            #time.sleep(1)

except KeyboardInterrupt:
    # Code to handle Ctrl+C and stop the program gracefully
    stop()
finally:
    # Cleanup GPIO resources
    GPIO.cleanup()
