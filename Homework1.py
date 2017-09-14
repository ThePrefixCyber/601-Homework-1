#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:46:14 2017

@author: Jack
"""

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--[image path]", required=True)
    default="cat"
ap.add_argument("-c", "--[cascade xml path]")
    default="haarcascade_frontalcatface.xml")