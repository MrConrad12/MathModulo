# ============ MATH MODULO ============

#Here's a brief Python program designed to visually represent the modulo operation of a number. Feel free to test it and make modifications as needed

"""
Modulo Visualization Program

This small Python program is aimed at providing a visual representation of the modulo operation. It utilizes the tkinter library for creating a graphical user interface.

Usage:
1. Run the program.
2. The program will display a canvas with a moving circular object.
3. Use the manual or automatic configuration options to adjust the modulo and multiplier values.
4. Click the "RUN" button in the "Auto config" section to start the animation with the specified parameters.
5. Click the "STOP" button to halt the animation.
6. You can also directly input modulo and multiplier values using the Spinbox inputs and activate or deactivate them with the checkboxes in the "Manual config" section.
7. To visualize the modulo operation, observe how the circular object moves within the canvas.

Feel free to experiment with different modulo and multiplier values, as well as animation speed. This program can serve as an educational tool to better understand the modulo operation and its graphical representation.
"""

from tkinter import *
from math import *
from graph import Graph
from control import Command
import matplotlib.pyplot as plt 
import numpy as np

