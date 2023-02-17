from machine import Pin, PWM
import time

pwm = PWM(Pin(25))

#Motor A
ma1 = Pin(10, Pin.OUT) #1
ma2 = Pin(11, Pin.OUT) #2
mas = Pin(12, Pin.OUT) #Enable

#Motor B
mb1 = Pin(21, Pin.OUT) #1
mb2 = Pin(20, Pin.OUT) #2
mbs = Pin(19, Pin.OUT) #Enable

# Construct PWM object, with LED on Pin(25).
pwm = PWM(Pin(25))

# Set the PWM frequency.
pwm.freq(1000)

def blinkey():
    duty = 0
    direction = 1
    for _ in range(8 * 256):
        duty += direction
        if duty > 255:
            duty = 255
            direction = -1
        elif duty < 0:
            duty = 0
            direction = 1
        pwm.duty_u16(duty * duty)
        time.sleep(0.001)

def blink():
    duty = 0
    direction = 1
    for _ in range(2 * 256):
        duty += direction
        if duty > 255:
            duty = 255
            direction = -1
        elif duty < 0:
            duty = 0
            direction = 1
        pwm.duty_u16(duty * duty)
        time.sleep(0.001)
    

def stop():
    ma1.value(0)
    ma2.value(0)
    mas.value(0)
    
    mb1.value(0)
    mb2.value(0)
    mbs.value(0)

def foreward():
    ma1.value(0)
    ma2.value(1)
    mas.value(1)
    
    mb1.value(0)
    mb2.value(1)
    mbs.value(1)
    
def backwards():
    ma1.value(1)
    ma2.value(0)
    mas.value(1)
    
    mb1.value(1)
    mb2.value(0)
    mbs.value(1)
    
def turn():
    ma1.value(1)
    ma2.value(0)
    mas.value(1)
    
    mb1.value(0)
    mb2.value(1)
    mbs.value(1)

# Fade the LED in and out a few times.
while True:
    blink()
    
    stop()
    time.sleep(3)
    blink()
    blink()
    
    foreward()
    time.sleep(20)
    blink()
    blink()
    blink()
    blink()
    
    stop()
    time.sleep(1)
    blink()
    blink()
    
    backward()
    time.sleep(1)
    blink()
    blink()
    blink()
    blink()
    
    stop()
    time.sleep(1)
    blink()
    blink()
    
    turn()
    time.sleep(3)
    blink()
    blink()
    blink()
    blink()
    
    
    

