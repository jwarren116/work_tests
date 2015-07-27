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

# assign closest camera match in known_cameras list to value in camera_map
# if a match is not found, assume not a valid camera
for camera in cameras:
    # n is number of results returned
    # cutoff is a float 0 (no similarity) to 1 (exact match)
    camera_result = get_close_matches(camera, known_cameras, n=1, cutoff=0.4)
    try:
        camera_map[camera] = camera_result[0]
    except IndexError:
        pass

print camera_map
