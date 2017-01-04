import cozmo
import time

def cozmo_program(robot: cozmo.robot.Robot):
    robot.move_head(-1)
    robot.move_lift(-1)
    robot.drive_wheels(50, 25)
    time.sleep(3)

    robot.move_head(1)
    robot.move_lift(1)
    robot.drive_wheels(50, -50)
    time.sleep(3)

cozmo.run_program(cozmo_program)
