"""
VPython 3D Animation
====================
Description: Simple VPython animation demo showing a red sphere moving across the screen. 
Demonstrates 3D visualization basics with VPython at 60 FPS.

Dependencies:
    pip3 install vpython

Author: Vilas
"""

from vpython import *
# Create the ball
ball = sphere(color=color.red)

# You MUST have this loop for the scene to stay alive
while True:
    rate(60) # Sets the speed to 60 FPS
    ball.pos.x = ball.pos.x + 0.01
