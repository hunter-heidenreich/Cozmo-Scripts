import cozmo
from cozmo.util import degrees

def cozmo_program(robot: cozmo.robot.Robot):

    for i in range(4):
        robot.say_text(str(i + 1)).wait_for_completed()

    for x in range(1, 5):
        robot.say_text(str(x * 90)).wait_for_completed()
        robot.turn_in_place(degrees(x * 90)).wait_for_completed()
    robot.say_text('All done').wait_for_completed()

cozmo.run_program(cozmo_program)
