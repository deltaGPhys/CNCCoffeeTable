# CNCCoffeeTable
Software to control CNC Zen Garden Coffee Table

This controls a coffee table that I built from a slab of black walnut. Sand is inset in the top of the table, with a steel ball bearing in it. 
Below that is a custom-built xy gantry with a magnet. As this moves, the ball is rolled through the sand, drawing patterns.
The gantry is controlled via Raspberry Pi and the Python software in this repo. A Django application serves an interface locally for the user to choose 
both patterns to clear the sand (tight sprial, horizontal strokes, vertical strokes, etc.) and then a design to draw on top of it. 
Designs are coded in GCODE, and the Django application serves those to the CNC controller.

## Photos
<img src = "https://github.com/deltaGPhys/CNCCoffeeTable/blob/master/Shape%20Paths/spirals.jpg" width="400px">
<img src = "https://github.com/deltaGPhys/CNCCoffeeTable/blob/master/Shape%20Paths/spiralsblue.png" width="400px">
<img src = "https://github.com/deltaGPhys/CNCCoffeeTable/blob/master/Shape%20Paths/maze.jpg" width="400px">
