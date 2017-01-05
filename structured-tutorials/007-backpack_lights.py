import cozmo
import time

def cozmo_program(robot: cozmo.robot.Robot):

    robot.set_all_backpack_lights(cozmo.lights.Light(on_color=cozmo.lights.Color(rgb=(75, 0, 130))))
    time.sleep(2)

    robot.set_all_backpack_lights(cozmo.lights.red_light)
    time.sleep(2)
    robot.set_all_backpack_lights(cozmo.lights.blue_light)
    time.sleep(2)
    robot.set_all_backpack_lights(cozmo.lights.green_light)
    time.sleep(2)
    robot.set_all_backpack_lights(cozmo.lights.white_light)
    time.sleep(2)
    robot.set_all_backpack_lights(cozmo.lights.off_light)
    time.sleep(2)

cozmo.run_program(cozmo_program)
