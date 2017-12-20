import pyximport

pyximport.install()

import cv2
import numpy as np

IMG_PATH = "img/sobeltest.png"


def image_to_greyscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def avg_blur(image, kernel_size=3):
    return cv2.blur(image, (kernel_size, kernel_size))


def gaussian_blur(image, kernel_size=3, sigma=0.0):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)


def transform_by_kernel(image, kernel):
    return cv2.filter2D(image, -1, kernel)


def canny_edge_detection(image, lower_threshold=210, upper_threshold=250):
    return cv2.Canny(gaussian_blur(image_to_greyscale(image)), lower_threshold, upper_threshold)


if __name__ == "__main__":
    img = cv2.imread(IMG_PATH)
    greyscale = image_to_greyscale(img)
    blurred = gaussian_blur(greyscale)
    canny = canny_edge_detection(img)

    cv2.imshow("normal", np.hstack([greyscale, blurred, canny]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
