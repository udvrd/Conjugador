import tkinter as tk

def draw_smiley(canvas):
    canvas.delete("all")
    x0, y0 = 10, 10
    canvas.create_oval(x0, y0, x0 + 100, y0 + 100, fill="#ffeb99", outline="black", width=2)
    canvas.create_oval(x0 + 25, y0 + 30, x0 + 35, y0 + 40, fill="black")
    canvas.create_oval(x0 + 65, y0 + 30, x0 + 75, y0 + 40, fill="black")
    canvas.create_arc(x0 + 25, y0 + 40, x0 + 75, y0 + 80, start=200, extent=140, style=tk.ARC, width=2)

def draw_sad_smiley(canvas):
    canvas.delete("all")
    x0, y0 = 10, 10
    canvas.create_oval(x0, y0, x0 + 100, y0 + 100, fill="#ffeb99", outline="black", width=2)
    canvas.create_oval(x0 + 25, y0 + 30, x0 + 35, y0 + 40, fill="black")
    canvas.create_oval(x0 + 65, y0 + 30, x0 + 75, y0 + 40, fill="black")
    canvas.create_arc(x0 + 25, y0 + 60, x0 + 75, y0 + 90, start=20, extent=140, style=tk.ARC, width=2)


def draw_thinking_smiley(canvas):
    canvas.delete("all")
    x0, y0 = 10, 10
    canvas.create_oval(x0, y0, x0 + 100, y0 + 100, fill="#ffeb99", outline="black", width=2)
    canvas.create_oval(x0 + 25, y0 + 30, x0 + 35, y0 + 40, fill="black")
    canvas.create_oval(x0 + 65, y0 + 30, x0 + 75, y0 + 40, fill="black")
    canvas.create_line(x0 + 25, y0 + 25, x0 + 35, y0 + 27, width=2)
    canvas.create_line(x0 + 65, y0 + 25, x0 + 75, y0 + 23, width=2)
    canvas.create_line(x0 + 40, y0 + 70, x0 + 70, y0 + 65, width=2)
