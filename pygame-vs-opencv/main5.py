import pyximport

pyximport.install()

import cv2
import timeit
import numpy as np

from lab2 import blur_utils as bu
from lab2 import pygame_utils as pgu
from lab3 import edge_utils as eu
from main2 import transform_by_kernel
from main3 import canny_edge_detection
import main4 as m4

IMG_PATH = "img/cat.jpg"
MEASUREMENTS = 20
SOBEL_SUM = 3.5

AVERAGES = {}
GAUSSIAN = {}
for i in range(1, 7, 2):
    AVERAGES[i] = bu.avg_kernel(i)
    GAUSSIAN[i] = bu.gaussian_kernel(i)


def measure_execution_time(fun, times=1):
    measure_points = []
    for _ in range(0, times):
        start = timeit.default_timer()
        fun()
        end = timeit.default_timer()
        measure_points.append(end - start)

    return measure_points


def print_measurements(source, measurements):
    for description in measurements:
        print("{},{},{},{}".format(source, description, np.mean(measurements[description]),
                                   np.std(measurements[description])))


def benchmark_lab2():
    """
    transform by kernel:
    - avg 1x1 3x3 5x5
    - gaussian 1x1 3x3 5x5
    """

    data_points = {}
    source_img = pgu.img_to_surface(IMG_PATH)

    for kernel_size in AVERAGES:
        data_points["average " + str(kernel_size)] = measure_execution_time(
            lambda: transform_by_kernel(source_img, AVERAGES[kernel_size]),
            MEASUREMENTS)

    for kernel_size in GAUSSIAN:
        data_points["gaussian " + str(kernel_size)] = measure_execution_time(
            lambda: transform_by_kernel(source_img, GAUSSIAN[kernel_size]),
            MEASUREMENTS)

    print_measurements("Pygame", data_points)


def benchmark_lab3():
    """
    img to greyscale
    canny without blur
    canny with blur
    """

    source_img = pgu.img_to_surface(IMG_PATH)
    data_points = {
        "greyscale": measure_execution_time(lambda: eu.surf_to_greyscale(source_img), MEASUREMENTS)}

    def canny(image, kernel=None):
        image = eu.surf_to_greyscale(image)
        if kernel is not None:
            image = transform_by_kernel(image, kernel)
        canny_edge_detection(image, SOBEL_SUM)

    def canny_without_blur():
        tag = "canny without blur"
        data_points[tag] = []
        for _ in range(MEASUREMENTS):
            img = pgu.img_to_surface(IMG_PATH)
            data_points[tag].append(measure_execution_time(lambda: canny(img))[0])

    def canny_with_blur():
        # with 3x3 gaussian kernel
        tag = "canny with 3x3 gaussian blur"
        data_points[tag] = []
        for _ in range(MEASUREMENTS):
            img = pgu.img_to_surface(IMG_PATH)
            data_points[tag].append(
                measure_execution_time(lambda: canny(img, GAUSSIAN[3]))[0])

    canny_without_blur()
    canny_with_blur()

    print_measurements("Pygame", data_points)


def benchmark_lab4():
    """
    transform by kernel:
    - avg 1x1 3x3 5x5
    - gaussian 1x1 3x3 5x5

    img to greyscale
    canny without blur
    canny with blur
    """

    data_points = {}
    img = cv2.imread(IMG_PATH)

    # blurring - transform by kernel using filter2D
    for kernel_size in AVERAGES:
        data_points["average filter2D " + str(kernel_size)] = measure_execution_time(
            lambda: m4.transform_by_kernel(img, AVERAGES[kernel_size][0] / AVERAGES[kernel_size][1]),
            MEASUREMENTS)

    for kernel_size in GAUSSIAN:
        data_points["gaussian filter2D " + str(kernel_size)] = measure_execution_time(
            lambda: m4.transform_by_kernel(img, GAUSSIAN[kernel_size][0] / GAUSSIAN[kernel_size][1]),
            MEASUREMENTS)

    # blurring using native cv2 methods
    for k in range(1, 7, 2):
        data_points["average native " + str(k)] = measure_execution_time(
            lambda: m4.avg_blur(img, k),
            MEASUREMENTS)
        data_points["gaussian native " + str(k)] = measure_execution_time(
            lambda: m4.gaussian_blur(img, k),
            MEASUREMENTS)

    # img to greyscale
    data_points["greyscale"] = measure_execution_time(lambda: m4.image_to_greyscale(img), MEASUREMENTS)

    # canny without blur
    data_points["canny without blur"] = measure_execution_time(lambda: m4.canny_edge_detection(img, False),
                                                               MEASUREMENTS)

    # canny with 3x3 gaussian blur
    data_points["canny with 3x3 gaussian blur"] = measure_execution_time(lambda: m4.canny_edge_detection(img, True),
                                                                         MEASUREMENTS)

    print_measurements("OpenCV", data_points)


if __name__ == "__main__":
    print("source, method, avg time, time std dev")
    benchmark_lab2()
    benchmark_lab3()
    benchmark_lab4()
