import sys
import time
from PIL import Image
import cozmo


def run(sdk_conn):
    # Connect to Cozmo and return an instance of the robot
    robot = sdk_conn.wait_for_robot()

    # Set all his mechanics for best screen viewing
    robot.set_lift_height(0.0).wait_for_completed()
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    # Create list of images to access
    image_settings = [("images/star.jpg", Image.NEAREST),
                      ("images/animal.jpg", Image.NEAREST),
                      ("images/male.jpg", Image.NEAREST)]

    # Loop through and prep all images for display
    face_images = []
    for image_name, resampling_mode in image_settings:
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,
                                                                 invert_image=True)
        face_images.append(face_image)

    # Display the images
    duration_s = 2.0
    for image in face_images:
        robot.display_oled_face_image(image, duration_s * 1000.0)
        time.sleep(duration_s)

    # Loop through and re-initialize the images, this time not inverted
    face_images = []
    for image_name, resampling_mode in image_settings:
        image = Image.open(image_name)
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,
                                                                 invert_image=False)
        face_images.append(face_image)

    # Display the images
    for image in face_images:
        robot.display_oled_face_image(image, duration_s * 1000.0)
        time.sleep(duration_s)


if __name__ == '__main__':
    cozmo.setup_basic_logging()
    try:
        cozmo.connect(run)
    except cozmo.ConnectionError as e:
        sys.exit("A connection error occurred: %s" % e)
