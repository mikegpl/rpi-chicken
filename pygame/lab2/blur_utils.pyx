def avg_kernel(size = 3):
    return [[1] * size for _ in range(0, 3)], size ** 2

# todo - gaussian kernel
# here

# transform pixel
cdef tuple ctransform_pixel(array, surface, int x, int y, int radius, int width, int height, kernel, int weight_sum):
    cdef int r_avg, g_avg, b_avg
    cdef int r, g, b, a
    cdef int multiplier
    
    multiplier = 1
    r_avg = g_avg = b_avg = 0


    for i in range(x - radius, x + radius + 1):
        for j in range(y - radius, y + radius + 1):
            if 0 <= i < width and 0 <= j < height:
                r, g, b, a = surface.unmap_rgb(array[i, j])
                multiplier = kernel[i -x + radius][j - y + radius]
                r_avg += r * multiplier
                g_avg += g * multiplier
                b_avg += b * multiplier                

    return int(r_avg / weight_sum), int(g_avg / weight_sum), int(b_avg / weight_sum)

cdef int crgb(surface, int rgba):
    cdef int r, g, b, a
    r, g, b, a = surface.unmap_rgb(rgba)
    return ((r & 255) << 16) | ((g & 255) << 8) | (b & 255)

cdef int crgb2int(int r, int g, int b):
    return ((r & 255) << 16) | ((g & 255) << 8) | (b & 255)

# wrappers
def transform_pixel(array, surface, x, y, radius, width, height, kernel, weight_sum):
    return ctransform_pixel(array, surface, x, y, radius, width, height, kernel, weight_sum)

def rgb(surface, rgba):
    return crgb(surface, rgba)

def rgb2int(r, g, b):
    return crgb2int(r, g, b)