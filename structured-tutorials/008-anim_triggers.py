import cozmo

def cozmo_program(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.FrustratedByFailure).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.PetDetectionCat).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.PetDetectionDog).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.Surprise).wait_for_completed()

cozmo.run_program(cozmo_program)
