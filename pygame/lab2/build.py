import os


print("Building cython files")
os.system("python3 setup.py build_ext --inplace")