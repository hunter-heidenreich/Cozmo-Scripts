import cozmo

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text('Hello World').wait_for_completed()
    robot.say_text('How is your day today?').wait_for_completed()
    robot.say_text('I am doing swell!').wait_for_completed()

cozmo.run_program(cozmo_program)
