#!/usr/bin/env python
import io
import re


camera_map = {}

# read contents of file into camera_list
camera_list = io.open('camera_list.txt', mode='r').readlines()

# strip extra whitespace and line breaks from each camera in list
cameras = [camera.strip() for camera in camera_list]

# converting to set and back to list removes duplicate values
cameras = list(set(cameras))

# iterate through camera list, map camera to title cased version
for camera in cameras:
    camera_map[camera] = camera

print len(camera_map)
