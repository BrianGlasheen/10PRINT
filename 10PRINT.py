import tkinter as tk 
from random import randint

SCREEN_SIZE = 800   # adjust gui size
SPACING = 10        # adjust spacing between lines
PERCENT_CHANCE = 50 # percent chance for left vs right line
                    # higher percent = higher right facing line count
root = tk.Tk()
root.wm_title("10PRINT")
root.wm_geometry(f"{SCREEN_SIZE}x{SCREEN_SIZE}")

canvas = tk.Canvas(root, width=SCREEN_SIZE, height=SCREEN_SIZE, background='black')
canvas.pack(side=tk.BOTTOM)

def ten_print(e):
    canvas.delete('all')
    density = SCREEN_SIZE//SPACING
    for y in range(0,SCREEN_SIZE,SPACING):
        for x in range(0,SCREEN_SIZE,SPACING): 
            if randint(0,100) > PERCENT_CHANCE:
                canvas.create_line(x, y, x+SPACING, y+SPACING, fill='white')
            else:
                canvas.create_line(x, y+SPACING, x+SPACING, y, fill='white')
            root.update()

root.bind("<Key>", ten_print)
root.mainloop()