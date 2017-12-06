'''
To be done:
Migrate to usage of 3d arrays of pixels [(x, y) -> int rgba to (x, y, index) -> double r/g/b]

Edge detection algorithm:
X, Y = image.to_grayscale().sobel(g_x(), g_y())
combine X and Y into one magnitude of gradient array G[x,y] = sqrt(X[x,y] ^ 2 + Y[x, y] ^2)
define two thresholds - upper and lower and perform canny algorithm:
if pixel value > upper -> set it to "hot" value
else if pixel value > lower -> if it is adjacent to any "hot" pixel mark it as "hot"
else -> discard pixel, set it to "cold" value

'''