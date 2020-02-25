# Write your code here :-)
from microbit import *
import random

display.scroll("Even or odd?")
display.scroll("Press B for even, A for odd")

while True:
    suprise = int(random.randint(1, 20))
    mod = suprise % 2
    display.scroll(suprise)

    while True:
        if (mod == 0):
            if (button_a.is_pressed()):
                display.show(Image.SAD)
                sleep(5000)
                break
            elif (button_b.is_pressed()):
                display.show(Image.HAPPY)
                sleep(5000)
                break
        else:
            if (button_a.is_pressed()):
                display.show(Image.HAPPY)
                sleep(5000)
                break
            elif (button_b.is_pressed()):
                display.show(Image.SAD)
                sleep(5000)
                break

    display.scroll("Cont?")
    if (button_b.is_pressed()):
        break


