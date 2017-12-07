from distutils.core import setup
from Cython.Build import cythonize

setup(name="edge_utils", ext_modules=cythonize('edge_utils.pyx'),)