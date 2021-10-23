from tkinter import *
import random
import time


def create_canvas(LS=160):
    tk = Tk()
    canvas = Canvas(tk, width=(LS + 1) * 5, height=760)
    canvas.pack()
    return tk, canvas


tk, canvas = create_canvas()
blocks = []
search_val = IntVar()
search_val.set(5)


class Block:
    is_selected = False

    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.h = y2 - y1
        self.pos = (x1 - 3) / 5
        self.img = canvas.create_rectangle(x1, y1, x2, y2, fill='red')

    def color_chk(self):
        if self.is_selected:
            canvas.itemconfig(self.img, fill='blue')
        else:
            canvas.itemconfig(self.img, fill='green')

    def select(self):
        self.is_selected = True
        self.color_chk()
        time.sleep(0.7)
        tk.update()

    def deselect(self):
        self.is_selected = False
        self.color_chk()
        time.sleep(0.7)
        tk.update()

    def found(self):
        canvas.itemconfig(self.img, fill='black')


def swap(b1, b2, list=None, tk=tk, canvas=canvas):
    if list is None:
        list = blocks
    list[b1].is_selected = True
    list[b2].is_selected = True
    list[b1].color_chk()
    list[b2].color_chk()
    tk.update()
    dist = list[b2].x1 - list[b1].x1
    canvas.move(list[b1].img, dist, 0)
    canvas.move(list[b2].img, -dist, 0)
    list[b1].x1 += dist
    list[b2].x1 -= dist
    list[b1].x2 += dist
    list[b2].x2 -= dist
    list[b1], list[b2] = list[b2], list[b1]
    tk.update()
    list[b1].pos, list[b2].pos = list[b2].pos, list[b1].pos
    list[b1].is_selected = False
    list[b2].is_selected = False
    list[b1].color_chk()
    list[b2].color_chk()
    time.sleep(0.007)
    tk.update()


def shuffle(LS=140, list=None, tk=tk, canvas=canvas):
    if list is None:
        list = blocks
    for i in range(0, LS):
        c = random.randrange(0, LS, 1)
        swap(i, c, list)


def generate(LS=140, list=None, canvas=canvas):
    if list is None:
        list = blocks
    for i in range(0, LS):
        list.append(Block(canvas, 3 + 5 * i, 0, 8 + 5 * i, 10 + 5 * i))


def reset():
    for b in blocks:
        canvas.itemconfig(b.img, fill='red')
