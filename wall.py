#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:52:30 2018

@author: jorge
"""

import os
import subprocess
import time
def cambio():
    wall = '/home/daniarch/Wallpapers/'
    os.chdir(wall)
    lswall = os.walk(wall)
    time.sleep(3)
    for root, name, files in lswall:
        for fil in files:
            (names, exten) = os.path.splitext(fil)
            if '.jpg' or '.png' in exten:
                subprocess.call(['feh', '--bg-fill', fil])
                time.sleep(500)
    cambio()

cambio()
