import sys
import RPi.GPIO as GPIO

# Register Pin number
enable1 = 22
input1a = 18
input1b = 16
led = 12

def control(arg):
    if arg == 'init':
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(enable1, GPIO.OUT)
        GPIO.setup(input1a, GPIO.OUT)
        GPIO.setup(input1b, GPIO.OUT)
        GPIO.setup(led, GPIO.OUT)

    elif arg == 'forward':
        GPIO.output(enable1, True)
        GPIO.output(input1a, True)
        GPIO.output(input1b, False)

    elif arg == 'backward':
        GPIO.output(enable1, True)
        GPIO.output(input1a, False)
        GPIO.output(input1b, True)

    elif arg == 'stop':
        GPIO.output(enable1, False)

    elif arg == 'on':
        GPIO.output(led, True)

    elif arg == 'off':
        GPIO.output(led, False)

    elif arg == 'quit':
        GPIO.cleanup()

    else:
        print 'No such command: ' + arg

if __name__ == '__main__':
    control('init')
    control(sys.argv[1])
