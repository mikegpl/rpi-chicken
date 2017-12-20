import pyximport

pyximport.install()

import resource
import numpy as np

from lab2 import blur_utils as bu
from lab2 import pygame_utils as pgu
from lab3 import edge_utils as eu
from main2 import transform_by_kernel
from main3 import canny_edge_detection

"""
Here will go benchmarking methods for ops coded for lab2 and lab3.

Plan:
1. Measure time per execution of surface processing methods to measure FPS:
    -on regular PC
    -on RPi
2. Use Pycharm's built-in profiler to get specific data about performance.
"""

IMG_PATH = "img/cat.jpg"
MEASUREMENTS = 2
SOBEL_SUM = 3.5


def measure_execution_time(fun, times=1):
    measure_points = []
    for _ in range(0, times):
        start = resource.getrusage(resource.RUSAGE_SELF)
        fun()
        end = resource.getrusage(resource.RUSAGE_SELF)
        system = end.ru_stime - start.ru_stime
        user = end.ru_utime - start.ru_utime
        measure_points.append((system, user))

    return measure_points


def benchmark_lab2():
    """
    transform by kernel:
    - avg 1x1 3x3 5x5
    - gaussian 1x1 3x3 5x5
    """

    data_points = {}

    source_img = pgu.img_to_surface(IMG_PATH)

    averages = {}
    gaussian = {}
    for i in range(1, 7, 2):
        averages[i] = bu.avg_kernel(i)
        gaussian[i] = bu.gaussian_kernel(i)

    for kernel_size in averages:
        data_points["Average " + str(kernel_size)] = measure_execution_time(
            lambda: transform_by_kernel(source_img, averages[kernel_size]),
            MEASUREMENTS)

    for kernel_size in gaussian:
        data_points["Gaussian " + str(kernel_size)] = measure_execution_time(
            lambda: transform_by_kernel(source_img, gaussian[kernel_size]),
            MEASUREMENTS)

    for key in data_points:
        print(key)
        points = list(zip(*data_points[key]))
        sys_points = list(points[0])
        usr_points = list(points[1])
        print("Avg sys: {}\tStdev sys: {}\t\nAvg usr: {}\tStdev usr: {}".format(np.mean(sys_points),
                                                                                np.std(sys_points),
                                                                                np.mean(usr_points),
                                                                                np.std(usr_points)))
        print("###")


def benchmark_lab3():
    source_img = pgu.img_to_surface(IMG_PATH)
    data_points = {"To greyscale": measure_execution_time(lambda: eu.surf_to_greyscale(source_img), MEASUREMENTS)}

    averages = {}
    gaussian = {}
    for i in range(1, 7, 2):
        averages[i] = bu.avg_kernel(i)
        gaussian[i] = bu.gaussian_kernel(i)

    def canny(image, kernel=None):
        image = eu.surf_to_greyscale(image)
        if kernel is not None:
            image = transform_by_kernel(image, kernel)
        canny_edge_detection(image, SOBEL_SUM)

    def canny_without_blur():
        data_points["Canny without blur"] = []
        for _ in range(MEASUREMENTS):
            img = pgu.img_to_surface(IMG_PATH)
            data_points["Canny without blur"].append(measure_execution_time(lambda: canny(img))[0])

    def canny_with_blur():
        def measure_with_kernels(tag, size_to_kernel_map):
            for kernel_size in size_to_kernel_map:
                key = tag + " " + str(kernel_size)
                data_points[key] = []
                for _ in range(MEASUREMENTS):
                    img = pgu.img_to_surface(IMG_PATH)
                    data_points[key].append(measure_execution_time(lambda: canny(img, averages[kernel_size]))[0])

        measure_with_kernels("Canny with avg blur", averages)
        measure_with_kernels("Canny with gaussian blur", gaussian)

    canny_without_blur()
    canny_with_blur()

    for key in data_points:
        print(key)
        points = list(zip(*data_points[key]))
        sys_points = list(points[0])
        usr_points = list(points[1])
        print("Avg sys: {}\tStdev sys: {}\t\nAvg usr: {}\tStdev usr: {}".format(np.mean(sys_points),
                                                                                np.std(sys_points),
                                                                                np.mean(usr_points),
                                                                                np.std(usr_points)))
        print("@@@")


if __name__ == "__main__":
    benchmark_lab2()
    benchmark_lab3()
