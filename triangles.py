from turtle import *
import turtle

# Sets 'side_length variable to 20
side_length = 20

# Outer loop to draw the number of triangles specified in the range
for triangle in range(4):
    # Inner loop to draw the triangles
    for side in range(3):
        forward(side_length)
        left(120)
    
    # Checks if we are on the last triangle (range with one parameter starts at 0, not 1)
    if triangle < 3:

        # Moves to top of current triangle and turns left
        left(60)
        forward(side_length)
        left(120)

        # Increases side length
        side_length = side_length + 20

        # Moves forward half of new side length to ensure point of triangle is in the center
        forward(side_length / 2)

        # Rotates 180 degrees ready to draw the next triangle
        right(180)
    
turtle.mainloop()