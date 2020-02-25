# Write your code here :-)
from microbit import *
import random

# display.scroll("Even or odd?")
# display.scroll("Press B for even, A for odd")
# display.scroll("shake to reset")

while True:
    suprise = int(random.randint(1, 20))
    mod = suprise % 2
    display.scroll(suprise)

    while True:
        if (mod == 0):
            if (button_a.is_pressed()):
                display.show(Image.SAD)
                break
            elif (button_b.is_pressed()):
                display.show(Image.HAPPY)
                break
        else:
            if (button_a.is_pressed()):
                display.show(Image.HAPPY)
                break
            elif (button_b.is_pressed()):
                display.show(Image.SAD)
                break

    display.scroll("Cont?")
    if (button_b.is_pressed()):
        break


# Write your code here :-)
