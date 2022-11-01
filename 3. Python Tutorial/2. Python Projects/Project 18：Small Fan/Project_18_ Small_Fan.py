from machine import Pin,PWM
import time

#Pin of each section of L293D and set as output 
IN1_Pin = 2
IN2_Pin = 15
ENA_Pin = 0 #Control the speed of the motor

# speed：speed，0-100
# direction: Rotation direction,1 is clockwise,0 stops,-1 counterclockwise
# speed_pin：Pin number that controls the start and stop of the motor
def motorRun(speed, direction, speed_pin, clockwise_pin, anti_clockwise_pin):
    if speed > 100: speed=100
    if speed < 0: speed=0
    in1 = Pin(anti_clockwise_pin, Pin.OUT)
    in2 = Pin(clockwise_pin, Pin.OUT)
    pwm = PWM(Pin(speed_pin))
    pwm.freq(50)
    pwm.duty(int(speed/100*4096))
    if direction < 0:
        in2.value(0)
        in1.value(1)
    if direction == 0:
        in2.value(0)
        in1.value(0)
    if direction > 0:
        in2.value(1)
        in1.value(0)

while True:
    motorRun(100, 1, ENA_Pin, IN2_Pin, IN1_Pin)
    time.sleep(5)
    motorRun(100, 0, ENA_Pin, IN2_Pin, IN1_Pin)
    time.sleep(2)
    motorRun(100, -1, ENA_Pin, IN2_Pin, IN1_Pin)
    time.sleep(5)
    motorRun(100, 0, ENA_Pin, IN2_Pin, IN1_Pin)
    time.sleep(2)