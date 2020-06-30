#!/bin/bash

xrandr --newmode "1920x1080_144.00"  452.50  1920 2088 2296 2672  1080 1083 1088 1177 -hsync +vsync && xrandr --addmode DisplayPort-0 1920x1080_144.00 && xrandr --output DisplayPort-0 --mode 1920x1080_144.00
