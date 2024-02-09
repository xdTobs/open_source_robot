from ev3dev.auto import * 

mL = LargeMotor('outA'); mL.stop_action = 'hold'

mL.run_to_rel_pos(position_sp= 840, speed_sp = 250)

mL.wait_while('running')