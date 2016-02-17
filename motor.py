import sys
import RPi.GPIO as GPIO

# Register Pin number
enable1 = 22
input1a = 18
input1b = 16

def control(arg):
    if arg == 'init':
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(enable1, GPIO.OUT)
        GPIO.setup(input1a, GPIO.OUT)
        GPIO.setup(input1b, GPIO.OUT)

    elif arg == 'forward':
        GPIO.output(enable1, true)
        GPIO.output(input1a, true)
        GPIO.output(input1b, false)

    elif arg == 'backward':
        GPIO.output(enable1, true)
        GPIO.output(input1a, false)
        GPIO.output(input1b, true)

    elif arg == 'stop':
        GPIO.output(enable1, false)

    elif arg == 'quit':
        GPIO.cleanup()

    else:
        print 'No such command: ' + arg

if __name__ == '__main__':
    control(sys.argv[1])
