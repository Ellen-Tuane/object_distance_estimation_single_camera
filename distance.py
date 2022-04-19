import math

# The object distance is defined as the distance of the desired object from the center of the lens
# The proposed object distance measurement is based on finding the closest point from the object to the
# bottom-center of the camera’s field of view.


def object_distance(w, h, x2, y2, camera_height, cp):
    # camera_height is the height of the camera from the ground
    # a is a known value obtained by measurement
    a = math.atan((w - y2) / (x2 - (h/2)))
    o = math.pi/2 + a

    # x2, y2 = int(bbox[2]), int(bbox[3])
    # x3, y3,x4,y4 are the converted image pixels into millimeters using the calibration factor
    # cp = 3104  # focal point from camera calibration/ calibration factor
    x3 = x2 * cp
    y3 = y2 * cp
    x4 = w * cp
    y4 = h/2 * cp
    b = math.sqrt(math.pow((x4 - x3), 2) + math.pow((y4 - y3), 2))

    # dh is the horizontal object distance from the camera
    # do id the oblique distance of the object from the camera
    dh = math.sqrt(math.pow(a, 2) + math.pow(b, 2) - (2 * a * b * math.cos(o)))
    do = math.sqrt(math.pow(dh, 2) + math.pow(camera_height, 2))
    return do / 10000


def distance_alternative(w, h, x2, y2, camera_height):
    a = math.atan((w - y2) / (x2 - (h/2)))
    o = math.pi/2 + a

    b = math.sqrt(math.pow(((h/2) - x2), 2) + math.pow((w - y2), 2))
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2) - (2 * a * b * math.cos(o)))
    do = math.sqrt(math.pow(c, 2) + math.pow(camera_height, 2))
    return do
