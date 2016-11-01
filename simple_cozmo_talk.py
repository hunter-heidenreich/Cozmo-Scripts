import sys
import cozmo

simple_phrase = "Hey there!"

def run(sdk_conn):
    robot = sdk_conn.wait_for_robot()

    # Default arguments
    robot.say_text(simple_phrase).wait_for_completed()

    # Excited version
    robot.say_text(simple_phrase, play_excited_animation=True).wait_for_completed()

    # Generic male voice
    robot.say_text(simple_phrase, use_cozmo_voice=False).wait_for_completed()

    # Slow by half
    robot.say_text(simple_phrase, duration_scalar=0.9).wait_for_completed()

    # Speed up by 2
    robot.say_text(simple_phrase, duration_scalar=3.6).wait_for_completed()

    # Modulating the pitch of voice. Plays at {-1, 0, 1}
    for x in range(-1, 2):
        robot.say_text(simple_phrase, voice_pitch=x).wait_for_completed()


if __name__ == '__main__':
    cozmo.setup_basic_logging()

    try:
        cozmo.connect(run)
    except cozmo.ConnectionError as e:
        sys.exit("A connection error occurred: %s" % e)
