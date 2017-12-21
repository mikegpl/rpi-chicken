from distutils.core import setup
from Cython.Build import cythonize

setup(name="blur_utils", ext_modules=cythonize('blur_utils.pyx'),)