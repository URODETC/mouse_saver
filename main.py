import sys
import time
from pynput.mouse import Controller, Listener

mouse = Controller()
x_max = 2047
y_max = 1151
x_vel = 1
y_vel = 1
x, y = mouse.position
while 1:
    if mouse.position != (x, y):
        sys.exit()
    if x <= 0 or x >= x_max:
        x_vel *= -1
    if y <= 0 or y >= y_max:
        y_vel *= -1
    x += x_vel
    y += y_vel

    mouse.move(x_vel, y_vel)
    time.sleep(0.002)
