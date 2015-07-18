#!/usr/bin/env python
import io
from difflib import get_close_matches


camera_map = {}

# read contents of file into camera_list and strip line breaks
cameras = io.open('camera_list.txt', mode='r').readlines()
cameras = [camera.strip() for camera in cameras]

# read in current list of known cameras and strip line breaks
known_cameras = io.open('known_cameras.txt', mode='r').readlines()
known_cameras = [camera.strip() for camera in known_cameras]

# converting to set and back to list removes duplicate values
cameras = list(set(cameras))

# assign closest match to camera in known_cameras list to value in camera_map
# if a match is not found, map value to None
for camera in cameras:
    camera_result = get_close_matches(camera, known_cameras, n=1, cutoff=0.4)
    try:
        camera_map[camera] = camera_result[0]
    except IndexError:
        camera_map[camera] = None

print camera_map
