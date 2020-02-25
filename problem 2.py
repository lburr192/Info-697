# Write your code here :-)
from microbit import *

Temp = (temperature())
Comp = (compass.heading())

while True:
    if (button_a.is_pressed()):
        display.scroll(Temp)
        print(Temp)
    display.scroll(Comp)
    print(Comp)
    file = open("codefile.csv", "w")
    file.write("Temp"  "," "Comp")
    sleep(10000)
