#########################################################################
### Date: 2017/11/9
### file name: tracingModule.py
### Purpose: this code has been generated for the five-way tracking sensor
###         to perform the decision of direction
#########################################################################

# =======================================================================
# import needed library
# =======================================================================
import getLine
import movement


def line_tracing():
    while True:
        movement.pwm_setup()
        line_check = getLine.get_line()
        if line_check == ['0', '1', '1', '1', '1']:
            movement.go_forward_infinite(5, 100, line_check)
        elif line_check == ['1', '0', '1', '1', '1']:
            movement.go_forward_infinite(55, 70, line_check)
        elif line_check == ['1', '1', '0', '1', '1']:
            movement.go_forward_infinite(60, 60, line_check)
        elif line_check == ['1', '1', '1', '0', '1']:
            movement.go_forward_infinite(70, 55, line_check)
        elif line_check == ['1', '1', '1', '1', '0']:
            movement.go_forward_infinite(100, 5, line_check)
        elif line_check == ['0', '0', '1', '1', '1']:
            movement.go_forward_infinite(40, 90, line_check)
        elif line_check == ['1', '0', '0', '1', '1']:
            movement.go_forward_infinite(60, 52, line_check)
        elif line_check == ['1', '1', '0', '0', '1']:
            movement.go_forward_infinite(52, 60, line_check)
        elif line_check == ['1', '1', '1', '0', '0']:
            movement.go_forward_infinite(90, 40, line_check)
        elif line_check == ['1', '1', '0', '0', '0']:
            movement.go_forward_infinite(50, 60, line_check)
        elif line_check == ['1', '0', '0', '0', '1']:
            movement.go_forward_infinite(60, 60, line_check)
        elif line_check == ['0', '0', '0', '1', '1']:
            movement.go_forward_infinite(60, 50, line_check)
        elif line_check == ['1', '1', '1', '1', '1']:
            movement.go_forward_infinite(60, 60, line_check)
        elif line_check == ['0', '0', '0', '0', '1']:
            movement.go_forward_infinite(70, 55, line_check)
        elif line_check == ['1', '0', '0', '0', '0']:
            movement.go_forward_infinite(55, 70, line_check)
        else:
            movement.stop()
