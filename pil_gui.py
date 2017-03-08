
from tkinter import *
from os import system
i = 0
def initWindow():
    window = Tk()
   # window.resizable(width=False, height=False)
    window.minsize(width=1000, height=750)
    return window



class LabeledEdit:
    def __init__(self, label, text):
        self.label = label
        self._text = text

    @property
    def text(self):
        txt = self._text.get("1.0",END).replace("\n", "")
        for char in txt:
            if char not in "0123456789/*-+%.":
                return txt
        return eval(txt)



class tkWindow:

    def __init__(self):
        self.wnd = initWindow()

    def addTextEdit(self, x, y, tx="Label", w=23, h=1):
        T = Text(self.wnd, height=h, width=w)
        T.insert(END, tx)
        T.place(x=x, y=y)
        return T

    def addLabel(self, x, y, text="Label"):
        T = Label(self.wnd, text=text)
        T.place(y=y, x=x)
        return T

    def addLabeledEdit(self, x, y, label="Label", text="", w=5, h=1):
        label = self.addLabel(x-2, y-20, label)
        text = self.addTextEdit(x, y, text, w, h)
        return LabeledEdit(label, text)

    def addButton(self, x, y, text, action):
        b = Button(self.wnd, text=text, command=action)
        b.place(x=x, y=y)
        return b

from PIL import Image


def getIter(z, itr):
    c = z
    for iteration in range(itr):
        z = z ** 2 + c
        if abs(z) >= 2:
            return iteration + 1
    return itr


def dist(x,y):
    if x>y:
        x,y = y,x

    return y - x


def setPixel(p1, p2):
    x,y = p1
    r,g,b = p2
    r = str(hex(r))[2:].zfill(2)
    g = str(hex(g))[2:].zfill(2)
    b = str(hex(b))[2:].zfill(2)
    c="{}{}{}".format(r,g,b)
    img.put("#{}".format(c), (x,y))

def fnc_gen2(name,w,h,xstart,xend,ystart,yend,iter, delic, xoff, yoff, perc):
    perc['text'] = "Awaiting..."
    from time import sleep
    sleep(0.5)

    num = (xsize+1)*(ysize+1)

    for y in range(ysize):
        ypart = (y / ysize) * ydist + yoff
        for x in range(xsize):
            xpart = (x / xsize) * xdist + xoff
            z = complex(xstart + xpart, ystart + ypart)

            jmp = getIter(z, iter)



            clr = (0,0,0)

            if not jmp%2: clr = 1, 1, 1
            if not jmp % 3: clr = 2, 2, 2
            if not jmp % 4: clr = 4, 4, 4
            if not jmp % 5: clr = 8, 8, 8
            if not jmp % 6: clr = 16, 16, 16
            if not jmp % 7: clr = 32, 32, 32
            if not jmp % 8: clr = 64,64,64
            if not jmp % 9: clr = 128,128,128
            if not jmp % 10: clr = 255,255,255

            pixels[x, y] = clr


    for y in range(ysize):
        ypart = (y / ysize) * ydist + yoff
        for x in range(xsize):
            xpart = (x / xsize) * xdist + xoff
            z = complex(xstart + xpart, ystart + ypart)

            jmp = getIter(z, iter)



            if jmp is None:
                pixels[x, y] = (0, 0, 0)

            else:
                a = abs(192-int(255*(jmp/iter)))
                b = abs(128-int(255*(jmp/iter)))
                c = abs(64-int(255*(jmp/iter)))
                if jmp>iter-5:
                    pixels[x, y] = (a,b,c)
    global i
    i+=40
    jmc = "C:/Users/Fero/Desktop/img"+str(i)+".bmp"

    img.save(jmc)
    perc['text'] = "100%"
    img.show()
pkg = tkWindow()

name = pkg.addLabeledEdit(20, 30, "Name:", "C:/test.bmp", 30, 1)
w = pkg.addLabeledEdit(20, 70, "Width:", "192", 15, 1)
h = pkg.addLabeledEdit(180, 70, "Height:", "108", 15, 1)
xstart = pkg.addLabeledEdit(20, 110, "xstart:", "-3", 15, 1)
xend = pkg.addLabeledEdit(180, 110, "xend:", "1", 15, 1)
ystart = pkg.addLabeledEdit(340, 110, "ystart:", "-1.125", 15, 1)
yend = pkg.addLabeledEdit(500, 110, "yend:", "1.125", 15, 1)
delic = pkg.addLabeledEdit(20, 150, "delic:", "0.95", 15, 1)
xoff = pkg.addLabeledEdit(180, 150, "xoff:", "0", 15, 1)
yoff = pkg.addLabeledEdit(340, 150, "yoff:", "0", 15, 1)
iter = pkg.addLabeledEdit(500, 150, "iter:", "20", 15, 1)

print(name.text, w.text, h.text, xstart.text, xend.text, ystart.text, yend.text, iter.text, delic.text,
      xoff.text, yoff.text)

delic = float(delic.text)
xsize = int(w.text)
ysize = int(h.text)
xstart = float(xstart.text) / delic
xend = float(xend.text) / delic
ystart = float(ystart.text) / delic
yend = float(yend.text) / delic
iter = int(iter.text)
img = Image.new('RGB', (xsize, ysize), "white")
pixels = img.load()
xdist = dist(xstart, xend)
ydist = dist(ystart, yend)
xoff = float(xoff.text)
yoff = float(yoff.text)

perc = pkg.addLabel(20, 230, "0%")
perc['text'] = "..."
gen = pkg.addButton(20, 190, "Generate", lambda: fnc_gen2(name,w,h,xstart,xend,ystart,yend,iter, delic,
                                                          xoff, yoff, perc))

pkg.wnd.mainloop()







