import sys
import time

try:
    from PIL import Image
except ImportError:
    sys.exit('You need to install PIL')

import cozmo

def setup_position(robot: cozmo.robot.Robot):
    if robot.lift_height.distance_mm > 45:
        with robot.perform_off_charger():
            robot.set_lift_height(0.0).wait_for_completed()

def cozmo_program(robot: cozmo.robot.Robot):
    setup_position(robot)
    raw_images = [('../images/animal.jpg', Image.BICUBIC),
                    ('../images/male.jpg', Image.BICUBIC),
                    ('../images/star.jpg', Image.BICUBIC)]
    face_images = []
    for name, mode in raw_images:
        img = Image.open(name)
        resize = img.resize(cozmo.oled_face.dimensions(), mode)
        face = cozmo.oled_face.convert_image_to_screen_data(resize, invert_image=True)
        face_images.append(face)

    num_loops = 10
    duration = 2
    for _ in range(num_loops):
        for image in face_images:
            robot.display_oled_face_image(image, duration * 1000.0)
            time.sleep(duration)

cozmo.run_program(cozmo_program)
