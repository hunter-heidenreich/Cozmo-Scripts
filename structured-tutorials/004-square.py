import cozmo
from cozmo.util import degrees, speed_mmps, distance_mm

def cozmo_program(robot: cozmo.robot.Robot):
    for _ in range(4):
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()

cozmo.run_program(cozmo_program)
