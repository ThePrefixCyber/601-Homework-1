#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:46:14 2017

@author: Jack
"""

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--[image path]",
    default="cat_00.jpg")
ap.add_argument("-c", "--[cascade xml path]",
    default="haarcascade_frontalcatface.xml")
args = vars(ap.parse_args())

image = cv2.imread(args["[image path]"])



#show the image, wait infinity time
cv2.imshow("Cat Image", image)
cv2.waitKey(0)