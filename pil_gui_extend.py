import tkinter
import os
from PIL import Image, ImageTk
logtype = "msg"
oldpath = ""
dircnt = 0
imgcnt = 0



class imgpack():
    def __init__(self, x, y, path):
        self.path = path
        self.x = x
        self.y = y

    def makecanvas(self, xsize, ysize):
        self.img = Image.new('RGB', (xsize, ysize), "black")
        self.pixels = self.img.load()

    def save(self, path):
        global oldpath,dircnt, imgcnt
        if oldpath != path:
            oldpath = path
            dircnt = 0
            imgcnt = 0
            get_dir_index(path)
        get_img_index(path)
        savepath = path +"/img_series_" + str(dircnt) + "/img_" + str(imgcnt) + ".bmp"
        self.img.save(savepath)

    def load(self, path):
        try:
            path = path + "/img_series_" + str(dircnt) + "/img_" + str(imgcnt) + ".bmp"
            image = Image.open(path)
            tkpi = ImageTk.PhotoImage(image)
            imglbl = tkinter.Label(pkg.wnd, image=tkpi)
            imglbl.image = tkpi
            imglbl.place(x=self.x, y=self.y)
        except ValueError:
            log("File %s not found" %path)











def get_img_index(path):
    global imgcnt

    full_file_paths = get_filepaths("%s./img_series_%d" % (path,dircnt))
    if not full_file_paths:
        return

    for f in full_file_paths:
        if f.endswith(".bmp"):
            ff = f.split("\\")[-1]
            if ff.startswith("img_"):
                num = int(ff.replace("img_", '').replace(".bmp", ''))
                if num >= imgcnt:
                    imgcnt = num + 1

def get_dir_index(path):
    global dircnt
    dirs = get_directories(path)
    if not os.path.isdir(path):
        os.system("mkdir %s" %path)


    for f in dirs:
        if f.startswith(path+"\\img_series_"):

            j = f.replace(path+"\\", "").replace("img_series_", "")
            j = int(j)
            if j >= dircnt:
                 dircnt = j + 1

    series="%s\img_series_%d" % (path,dircnt)
    startpoint = path+"\\img_series_0"
    if not os.path.isdir(startpoint):
        series= startpoint
        dircnt = 0

    log(series)

    if not os.path.isdir(series):
        os.system("mkdir %s" % series)

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
        text = str(text)
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

pkg = tkWindow()