#inspired from Michele Simoniato

import random
import threading
import time

from Tkinter import *

WIDTH = 500
PARTS = 100

r = 2

def main():

    root = Tk()
    the_world = Canvas(root, width = WIDTH, height = WIDTH)
    the_world.pack(fill = "both", expand=1)
    for i in range(PARTS):
        thrd = threading.Thread(target = brown, args=(the_world,))
        thrd.start()
    root.mainloop()

def brown(the_world):

    x = random.randint(200, 250)
    y = random.randint(200, 250)
    left, up, right, down = x-r, y-r, x+r, y+r
    world = the_world.create_oval(left, up, right, down, fill="blue")
    while True:
        dx = random.gauss(0, 2)
        dy = random.gauss(0, 2)
        try:
            the_world.move(world, dx, dy)
        except TclError:
            break
            thrd.join()
        time.sleep(0.03)

if __name__ =="__main__":
    main()
