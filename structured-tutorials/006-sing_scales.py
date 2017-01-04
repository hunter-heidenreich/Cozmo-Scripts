import cozmo
from cozmo.util import degrees

def cozmo_program(robot: cozmo.robot.Robot):
    scale = ['Doe', 'Ray', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Doe']

    voice_pitch = -1.0
    voice_pitch_delta = 2 / (len(scale) - 1)

    robot.move_head(-5)
    robot.set_lift_height(0.0).wait_for_completed()
    robot.set_head_angle(degrees(-25)).wait_for_completed()

    robot.move_head(0.15)
    robot.move_lift(0.15)

    for note in scale:
        robot.say_text(note, voice_pitch=voice_pitch, duration_scalar=0.3).wait_for_completed()
        voice_pitch += voice_pitch_delta

cozmo.run_program(cozmo_program)
