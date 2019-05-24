"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Isabella Popoff.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 5)
red_turtle.speed = 10

green_turtle = rg.SimpleTurtle('turtle')
green_turtle.pen = rg.Pen('green', 7)
green_turtle.speed = 10

size = 50

for k in range(8):
    red_turtle.draw_circle(size)
    red_turtle.pen_up()
    red_turtle.forward(10)

    red_turtle.pen_down()
    size = size - 14

    green_turtle.draw_circle(size)
    green_turtle.pen_up()
    green_turtle.left(90)
    green_turtle.forward(20)

    green_turtle.pen_down()
    size = size - 14


window.close_on_mouse_click()
