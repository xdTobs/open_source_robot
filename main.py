from turtle import speed
from ev3dev.auto import * 

mL = LargeMotor('outA'); mL.stop_action = 'hold'

mL.run_forever(speed_sp = 250)

mL.wait_while('running')