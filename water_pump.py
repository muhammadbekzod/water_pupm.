import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for motor PWM and relay control
motor_pwm_pin = 18  # PWM control pin
relay_control_pin = 17  # GPIO pin connected to the relay control signal (D)

# Set up the GPIO pins
GPIO.setup(motor_pwm_pin, GPIO.OUT)
GPIO.setup(relay_control_pin, GPIO.OUT)

# Set up PWM on motor_pwm_pin with a frequency and duty cycle
pwm_frequency = 1000  # 1000 Hz
pwm_duty_cycle = 50  # 50% duty cycle

pwm = GPIO.PWM(motor_pwm_pin, pwm_frequency)
pwm.start(pwm_duty_cycle)

try:
    while True:
        # Motor control (PWM)
        # Your motor control logic goes here
        # For example, you can change the duty cycle to control motor speed
        # pwm.ChangeDutyCycle(new_duty_cycle)

        # Relay control
        GPIO.output(relay_control_pin, GPIO.HIGH)  # Turn the relay on

        # You can add a delay here if needed
        time.sleep(2)

        GPIO.output(relay_control_pin, GPIO.LOW)  # Turn the relay off

        # You can add another delay here if needed
        time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO settings
    pwm.stop()
    GPIO.cleanup()
