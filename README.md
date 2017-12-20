# rpi-chicken
##
Why did the chicken cross the road?

## Table of contents

* Pygame
    - lab1 Simple live capture with thresholding - (16.11.17)
    - lab2 First implementation of pixel-by-pixel filtering, with some debugging to be done - (23.11.17)
    - lab3 
        - Implementation of Canny edge detection algorithm (7.12.17)
        - Debugging, tuning for better performance (14.12.17)
* OpenCV 
    - lab4 OpenCV implementation of image processing implemented in Pygame.lab2-lab3 (14.12.17)
* Comparison
    - lab5 Benchmarking lab2-lab4 (14.12.17 - 21.12.17)
    
    

## Requirements
Following Python 3 modules are required:

* Pygame
* cython

## Setup
If files in lab* directory require any building/compilation use `python3 build.py` and `python3 clean.py` to build and clean the directory accordingly.



## Sources
Sources based on:

* lab1 - simple processing of image from camera

    http://pygame.org/docs/tut/CameraIntro.html

* lab2 - smoothing filters

    https://www.pygame.org/docs/ref/pixelarray.html

    http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html

* lab3 - Canny edge detection
    
    https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html
    
    https://en.wikipedia.org/wiki/Canny_edge_detector#Process_of_Canny_edge_detection_algorithm
    
* lab4 - OpenCV docs and previous research done for lab2-lab3
    
    
    
