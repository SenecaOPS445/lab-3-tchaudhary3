#!/usr/bin/env python3
'''Lab 3 Part 4 - Get free disk space on root directory'''
# Author ID: tchaudhary3

import subprocess

def free_space():
    # Execute the df command and capture the output
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, capture_output=True, text=True)
    
    # Return the free space value with stripped newlines
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())
