import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np
import os
import sys
import screeninfo
import time


def si(img_path, Squarized_img):

    base_name, ext = os.path.splitext(img_path)

    result, encoded_img = cv2.imencode(ext, Squarized_img)

    if result:

        encoded_img.tofile(base_name + ext)
        print(f"Image saved to {base_name + ext}")
    else:
        print("Error encoding image")


def cv_imread(file_path):

    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    return cv_img


print(
    """::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:::::::::::::
:::::::::::::,...:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::,...::::::::::::
:::::::::::::,..,::::::::::::::::::::::::::::::::,,,,::::::::::::::,,::::::::::::::::...::::::::::::
:::::::::::::,..,:::::::::::::::::::::::,,,...::,....::,...,,,,......::::::::::::::::...::::::::::::
:::::::::::::,..,::::::::::::::::::,,....,,,::::,....:::,,,..........::::::::::::::::...::::::::::::
:::::::::::::,..,::::::::::::::::,......::::::::,....:::::::::,......::::::::::::::::...::::::::::::
:::::::::::::,..,::::::::::::::::.......,,::::::,....::::::::::::,...::::::::::::::::...::::::::::::
:::::::::::::,..,:::::::::::::::::,..........,,,,,,,,::::::::::::::,.::::::::::::::::...::::::::::::
::::::::::::::,.,:::::::::::::::::::::,,,,..............,,,,:::::::::::::::::::::::::,.,::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::,,,,,...........,,::::::::::::::::::::::::::::::::::
:::::::::::::,..,:::::::::::::::,.,:::::::::::::,.,,,:::::,,........,::::::::::::::::...::::::::::::
:::::::::::::,..,:::::::::::::::,...,,::::::::::,....:::::::::.......::::::::::::::::...::::::::::::
:::::::::::::,..,:::::::::::::::,......,,,::::::,....::::::::,.....,:::::::::::::::::...::::::::::::
:::::::::::::,..,:::::::::::::::,.............::,....:::.......,,::::::::::::::::::::...::::::::::::
:::::::::::::,..,:::::::::::::::,.......,,,,,,::,....:::,,,::::::::::::::::::::::::::...::::::::::::
:::::::::::::,..,:::::::::::::::,..,::::::::::::,....::::::::::::::::::::::::::::::::...::::::::::::
:::::::::::::,..,:::::::::::::::::::::::::::::::::,,:::::::::::::::::::::::::::::::::...::::::::::::
:::::::::::::,...,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,...::::::::::::
:::::::::::::::,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""
)

print()
print("「One-Way Release License」")
print()
print("Contributed by Startemplib~")
print()


def centralize(tw, th):

    screen = screeninfo.get_monitors()[0]
    screen_width = screen.width
    screen_height = screen.height

    max_width = round(0.6 * screen_width)
    max_height = round(0.7 * screen_height)

    scale_factor = 1.0
    trig = []

    while True:
        scaled_width = round(tw * scale_factor)
        scaled_height = round(th * scale_factor)

        if scaled_width <= max_width and scaled_height <= max_height:
            scale_factor += 0.05
            trig.append("up")

        else:
            scale_factor -= 0.05
            trig.append("down")

        if len(trig) > 2 and trig[-1] != trig[-2]:
            break

    final_width = round(tw * scale_factor)
    final_height = round(th * scale_factor)

    x_pos = (screen_width - final_width) // 2
    y_pos = (screen_height - final_height) // 2

    return final_width, final_height, x_pos, y_pos


def mouse_callback(event, x, y, flags, param):

    param["mouse_x"], param["mouse_y"] = x, y
    pos = param["pos"]
    img_height, img_width = image.shape[:2]
    x = round((x + pos[0]) / param["zoom_factor"])
    y = round((y + pos[1]) / param["zoom_factor"])

    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            param["zoom_factor"] += 0.17
        else:
            param["zoom_factor"] = max(0.1, param["zoom_factor"] - 0.17)

    if event == cv2.EVENT_LBUTTONDOWN:

        points.append([x, y])

        img_height, img_width = img.shape[:2]
        size_factor = img_width / 700
        point_radius = int(3 * size_factor)
        font_scale = 0.5 * size_factor
        font_thickness = int(1 * size_factor)

        if ii == 0:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)

        cv2.line(image, (x - point_radius, y), (x + point_radius, y), color, 2)
        cv2.line(image, (x, y - point_radius), (x, y + point_radius), color, 2)
        cv2.putText(
            image,
            str(len(points)),
            (x + 5, y - 5),
            cv2.FONT_HERSHEY_COMPLEX,
            font_scale,
            color,
            font_thickness,
        )


def adjust_to_mouse_center(img_cv, zoom_factor, mouse_x, mouse_y):
    h, w, _ = img_cv.shape
    relative_mouse_x = mouse_x / ws[0]
    relative_mouse_y = mouse_y / ws[1]
    new_w = int(w * zoom_factor)
    new_h = int(h * zoom_factor)

    background = np.ones((ws[1], ws[0], 3), dtype=np.uint8) * 255
    resized = cv2.resize(img_cv, (new_w, new_h))

    start_x = max(0, int(relative_mouse_x * new_w - ws[0] // 2))
    start_y = max(0, int(relative_mouse_y * new_h - ws[1] // 2))
    end_x = min(start_x + ws[0], new_w)
    end_y = min(start_y + ws[1], new_h)

    cropped_resized = resized[start_y:end_y, start_x:end_x]
    background[0 : cropped_resized.shape[0], 0 : cropped_resized.shape[1]] = (
        cropped_resized
    )

    coordinates = [start_x, start_y, end_x, end_y]
    return background, coordinates


def get_image_path():

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image Files", "*.png;*.jpg;*")],
    )
    return file_path


if len(sys.argv) < 2:
    print("No image path provided.")
    print("Opening file manager to select an image...")

    img_path = ""
    img_path = get_image_path()

    if not img_path:
        print("No image selected, Bye~")
        time.sleep(1)
        sys.exit(1)


else:
    img_path = sys.argv[1]

img = cv_imread(img_path)
image = cv_imread(img_path)

state = "SELECT_POINTS"
points = []

print()

print("i: Inverse (invert the color)")
print("c: Continue (proceed with the squarization)")
print("b: Backward (reselect four points)")
print("s: Save (save the squarized image in the same folder)")
print("r: Replace (replace the original image)")
print("q: Quit (exit the program)")

ii = 0

while True:
    if state == "SELECT_POINTS":

        window_name = "Original Image"
        img_height, img_width = image.shape[:2]
        final_width, final_height, x_pos, y_pos = centralize(img_width, img_height)

        ws = (final_width, final_height)
        wp = (x_pos, y_pos)

        param = {
            "zoom_factor": 1,
            "mouse_x": 0,
            "mouse_y": 0,
            "pos": [],
        }

        zoom_factor = min(ws[0] / img_width, ws[1] / img_height)

        param["zoom_factor"] = zoom_factor

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.moveWindow(window_name, *wp)
        cv2.resizeWindow(window_name, *ws)

        while True:

            key = cv2.waitKey(1) & 0xFF

            if key == ord("c"):
                if len(points) == 4:
                    state = "TRANSFORM"
                    cv2.destroyAllWindows()
                    break

                else:
                    cv2.destroyAllWindows()
                    print("Please select exactly 4 points.")

                    image = cv_imread(img_path)
                    if points != []:
                        for i, (x, y) in enumerate(points):

                            img_height, img_width = img.shape[:2]
                            while True:
                                rate = 700

                                size_factor = img_width / rate

                                point_radius = int(3 * size_factor)
                                font_scale = 0.5 * size_factor
                                font_thickness = int(1 * size_factor)

                                if point_radius != 0:
                                    break
                                else:
                                    rate + 1

                            cv2.line(
                                image,
                                (x - point_radius, y),
                                (x + point_radius, y),
                                (0, 0, 255),
                                2,
                            )
                            cv2.line(
                                image,
                                (x, y - point_radius),
                                (x, y + point_radius),
                                (0, 0, 255),
                                2,
                            )

                    cv2.imshow("Original Image", image)
                    points = []

            elif key == ord("q"):
                sys.exit(1)

            elif key == ord("i"):
                ii = 1 if ii == 0 else 0

            adjusted_img, param["pos"] = adjust_to_mouse_center(
                image, param["zoom_factor"], param["mouse_x"], param["mouse_y"]
            )
            cv2.imshow(window_name, adjusted_img)

            cv2.setMouseCallback(window_name, mouse_callback, param)

    elif state == "TRANSFORM":

        points_array = np.array(points, dtype=np.float32)

        area = cv2.contourArea(points_array)

        width = 0.5 * (
            np.linalg.norm(points_array[1] - points_array[0])
            + np.linalg.norm(points_array[3] - points_array[2])
        )
        height = 0.5 * (
            np.linalg.norm(points_array[2] - points_array[1])
            + np.linalg.norm(points_array[3] - points_array[0])
        )
        aspect_ratio = width / height

        th = int(np.sqrt(area / aspect_ratio))
        tw = int(np.sqrt(area * aspect_ratio))

        src_points = np.float32(points)
        dst_points = np.float32([[0, 0], [tw, 0], [tw, th], [0, th]])

        M = cv2.getPerspectiveTransform(src_points, dst_points)
        Squarized_img = cv2.warpPerspective(img, M, (tw, th))

        cv2.namedWindow("Squarized Image", cv2.WINDOW_NORMAL)

        final_width, final_height, x_pos, y_pos = centralize(tw, th)

        cv2.resizeWindow("Squarized Image", final_width, final_height)
        cv2.moveWindow("Squarized Image", x_pos, y_pos)

        cv2.imshow("Squarized Image", Squarized_img)

        key = cv2.waitKey(0) & 0xFF

        if key == ord("s"):

            base_name, ext = os.path.splitext(img_path)
            new_img_path = base_name + "_squarized" + ext
            si(new_img_path, Squarized_img)
            print(f"Squarized image saved to: {new_img_path}")
            cv2.destroyAllWindows()
            break

        if key == ord("r"):

            base_name, ext = os.path.splitext(img_path)
            new_img_path = base_name + ext
            si(new_img_path, Squarized_img)
            print(f"Squarized image replaced: {new_img_path}")
            cv2.destroyAllWindows()
            break

        elif key == ord("b"):

            state = "SELECT_POINTS"

            image = cv_imread(img_path)

            print("Points reset, please select 4 new points.")

            for i, (x, y) in enumerate(points):

                img_height, img_width = img.shape[:2]

                size_factor = img_width / 700

                point_radius = int(3 * size_factor)
                font_scale = 0.5 * size_factor
                font_thickness = int(1 * size_factor)

                if ii == 0:
                    color = (0, 255, 255)
                else:
                    color = (255, 255, 0)

                cv2.line(image, (x - point_radius, y), (x + point_radius, y), color, 2)
                cv2.line(image, (x, y - point_radius), (x, y + point_radius), color, 2)

            cv2.imshow("Original Image", image)
            points = []

        elif key == ord("q"):
            break


cv2.destroyAllWindows()
