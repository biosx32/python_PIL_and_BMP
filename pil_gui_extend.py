import tkinter
import os
logtype = "msg"

def log(*msg):
    if logtype == "msg":
        print("LOG: ",*msg)

def get_filepaths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def get_directories(directory):
    dirs_paths = []
    for root, directories, files in os.walk(directory):
        for dir_o in directories:
            dirr = os.path.join(root, dir_o)
            dirs_paths.append(dirr)
    return dirs_paths


def initWindow():
    window = tkinter.Tk()
    # window.resizable(width=False, height=False)
    window.minsize(width=1000, height=750)
    return window


class LabeledEdit:
    def __init__(self, label, text, acctype):
        self.label = label
        self._text = text
        self._default_val =  self._text.get("1.0", tkinter.END).replace("\n", "")
        self._acctype = acctype

    @property
    def txv(self):  # text and value
        return  self.label['text'] + " " +str(self.value)

    def can_convert(self, x, type):
        try:
            y = type(x)
            return True
        except (TypeError, ValueError):
            return None

    @property
    def value(self):
        txt = self._text.get("1.0", tkinter.END).replace("\n", "")
        t = self._acctype
        if t == "all":
            return txt

        if not self.can_convert(txt, t):
            log("Cannot convert "+self.label['text'], txt, "to type ", t)
            self._text.insert(tkinter.END, self._default_val)
            txt = self._text.get("1.0", tkinter.END).replace("\n", "")
            print(txt)
            return t(txt)

        return t(txt)


class tkWindow:
    def __init__(self):
        self.wnd = initWindow()

    def addTextEdit(self, x, y, tx="Label", w=23, h=1):
        T = tkinter.Text(self.wnd, height=h, width=w)
        T.insert(tkinter.END, tx)
        T.place(x=x, y=y)
        return T

    def addLabel(self, x, y, text="Label", photo=None):
        T = tkinter.Label(self.wnd, text=text, photo=None )
        T.place(y=y, x=x)
        return T

    def addLabeledEdit(self, x, y, label="Label", text="", w=5, h=1, acctype="all"):
        label = self.addLabel(x - 2, y - 20, label)
        text = self.addTextEdit(x, y, text, w, h)
        return LabeledEdit(label, text, acctype)

    def addButton(self, x, y, text, action):
        b = tkinter.Button(self.wnd, text=text, command=action)
        b.place(x=x, y=y)
        return b



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