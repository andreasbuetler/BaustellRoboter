## circuit python code for motor control
import board
import digitalio

# set up the motor control pins
# Motor A
ma1 = digitalio.DigitalInOut(board.GP10)
ma1.direction = digitalio.Direction.OUTPUT
ma2 = digitalio.DigitalInOut(board.GP11)
ma2.direction = digitalio.Direction.OUTPUT
mas = digitalio.DigitalInOut(board.GP12)
mas.direction = digitalio.Direction.OUTPUT

# Motor B
mb1 = digitalio.DigitalInOut(board.GP21)
mb1.direction = digitalio.Direction.OUTPUT
mb2 = digitalio.DigitalInOut(board.GP20)
mb2.direction = digitalio.Direction.OUTPUT
mbs = digitalio.DigitalInOut(board.GP19)
mbs.direction = digitalio.Direction.OUTPUT

def stop():
    ma1.value = False
    ma2.value = False
    mas.value = False
    
    mb1.value = False
    mb2.value = False
    mbs.value = False

def foreward():
    ma1.value = False
    ma2.value = True
    mas.value = True
    
    mb1.value = False
    mb2.value = True
    mbs.value = True

def backwards():
    ma1.value = True
    ma2.value = False
    mas.value = True
    
    mb1.value = True
    mb2.value = False
    mbs.value = True
    
def turnRight():
    ma1.value = True
    ma2.value = False
    mas.value = True
    
    mb1.value = False
    mb2.value = True
    mbs.value = True

def turnLeft():
    ma1.value = False
    ma2.value = True
    mas.value = True
    
    mb1.value = True
    mb2.value = False
    mbs.value = True