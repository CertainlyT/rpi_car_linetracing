#########################################################################
### Date: 2017/10/13
### file name: trackingModule.py
### Purpose: this code has been generated for the five-way tracking sensor
###         to perform the decision of direction
###
#########################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
import getLine
import movement


try:
    while True:
        movement.pwm_setup()
        line_check = getLine.get_line()
        print(line_check)
        if line_check == ['0', '0', '0', '0', '0']:
            movement.stop()
        elif line_check == ['0', '1', '1', '1', '1']:
            movement.go_forward_infinite(25, 90, line_check)
        elif line_check == ['1', '0', '1', '1', '1']:
            movement.go_forward_infinite(35, 90, line_check)
        elif line_check == ['1', '1', '0', '1', '1']:
            movement.go_forward_infinite(60, 60, line_check)
        elif line_check == ['1', '1', '1', '0', '1']:
            movement.go_forward_infinite(90, 35, line_check)
        elif line_check == ['1', '1', '1', '1', '0']:
            movement.go_forward_infinite(90, 25, line_check)
        elif line_check == ['0', '0', '1', '1', '1']:
            movement.go_forward_infinite(30, 100, line_check)
        elif line_check == ['1', '0', '0', '1', '1']:
            movement.go_forward_infinite(60, 55, line_check)
        elif line_check == ['1', '1', '0', '0', '1']:
            movement.go_forward_infinite(55, 60, line_check)
        elif line_check == ['1', '1', '1', '0', '0']:
            movement.go_forward_infinite(100, 30, line_check)
        elif line_check == ['1', '1', '1', '1', '1']:
            movement.go_forward_infinite(30, 100, line_check)
        else:
            movement.stop()

               
except KeyboardInterrupt:
    movement.pwm_low()
    GPIO.cleanup()


