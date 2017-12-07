import numpy as np

def avg_kernel(size = 3):
    return np.ones((size, size)), size ** 2

def gaussian_kernel(size = 3, sigma = 1.0):
    ax = np.arange(-size // 2 + 1., size // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)
    kernel = 4.0 * np.exp(-(xx ** 2 + yy ** 2) / (2. * sigma ** 2))
    return kernel, np.sum(kernel)

# edge detection 
def gx():
    return np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]), 1

def gy():
    return np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]), 1

# using surface.pixels3d
def to_grayscale(pixel_array_3d):
    return pixel_array_3d.dot([0.298, 0.587, 0.114])[:, :, None].repeat(3, axis=2)

def mask_pixel(array, x, y, mask):
    size, _ = mask.shape

    for i in range(x - size, x + size + 1):
        for j in range(y - size, y + size + 1):
            pass

# transform pixel
cdef tuple ctransform_pixel(array, int x, int y, int radius, int width, int height, kernel, double weight_sum):
    cdef int r_avg, g_avg, b_avg
    cdef int r, g, b, a
    cdef int multiplier

    multiplier = 1
    r_avg = g_avg = b_avg = 0

    for i in range(x - radius, x + radius + 1):
        for j in range(y - radius, y + radius + 1):
            if 0 <= i < width and 0 <= j < height:
                r, g, b = array[i, j]
                multiplier = kernel[i - x + radius][j - y + radius]
                r_avg += r * multiplier
                g_avg += g * multiplier
                b_avg += b * multiplier
    return r_avg / weight_sum, g_avg / weight_sum, b_avg / weight_sum

# wrappers
def transform_pixel(array, x, y, radius, width, height, kernel, weight_sum):
    return ctransform_pixel(array, x, y, radius, width, height, kernel, weight_sum)
