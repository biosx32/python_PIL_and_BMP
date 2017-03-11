from pil_gui_extend import *
from PIL import Image, ImageTk
import os

# make time elapsed
# make time remaining
# make time expected



dircnt = 0
imgcnt = 0

oldpath = ""



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








def get_dir_index(path):
    global dircnt
    dirs = get_directories(path)
    if not os.path.isdir(path):
        os.system("mkdir %s" %path)


    for f in dirs:
        if f.startswith(path):
            j = f.replace(path+"\\", "").replace("img_series_", "")
            j = int(j)
            if j >= dircnt:
                 dircnt = j + 1

    series="%s\img_series_%d" % (path,dircnt)
    startpoint = path+"\\img_series_0"
    if not os.path.isdir(startpoint):
        series= startpoint
        dircnt = 0

    print(series)

    if not os.path.isdir(series):
        os.system("mkdir %s" % series)




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


pkg = tkWindow()

gui_filename_edit = pkg.addLabeledEdit(20, 30, "Name:", "E:\\test.bmp", 37, 0)
gui_width_edit = pkg.addLabeledEdit(20, 70, "Width:", "192", 7, 1, int)
gui_height_edit = pkg.addLabeledEdit(180, 70, "Height:", "108", 7, 1, int)
gui_width_m_edit = pkg.addLabeledEdit(100, 70, "WMulti:", "1", 7, 1, float)
gui_height_edit_m = pkg.addLabeledEdit(260, 70, "HMulti:", "1", 7, 1, float)
gui_xstart_edit = pkg.addLabeledEdit(20, 110, "xstart:", "-3", 7, 1, float)
gui_xend_edit = pkg.addLabeledEdit(100, 110, "xend:", "1", 7, 1, float)
gui_ystart_edit = pkg.addLabeledEdit(180, 110, "ystart:", "-1.125", 7, 1, float)
gui_yend_edit = pkg.addLabeledEdit(260, 110, "yend:", "1.125", 7, 1, float)
gui_divide_edit = pkg.addLabeledEdit(20, 150, "delic:", "1", 7, 1, float)
gui_xoff_edit = pkg.addLabeledEdit(100, 150, "xoff:", "0.0", 7, 1, float)
gui_yoff_edit = pkg.addLabeledEdit(180, 150, "yoff:", "0.0", 7, 1, float)
gui_iterations_edit = pkg.addLabeledEdit(260, 150, "iter:", "20", 7, 1, int)
gui_percentage_lbl = pkg.addLabel(20, 230, "...")
gui_generate_button = pkg.addButton(20, 190, "Generate", lambda: generate_from_gui())

gui2_filename_edit = pkg.addLabeledEdit(20 + 350, 30, "Name:", "E:\\test.bmp", 37, 0)
gui2_width_edit = pkg.addLabeledEdit(20 + 350, 70, "Width:", "192", 7, 1, int)
gui2_height_edit = pkg.addLabeledEdit(180 + 350, 70, "Height:", "108", 7, 1, int)
gui2_width_m_edit = pkg.addLabeledEdit(100 + 350, 70, "WMulti:", "1", 7, 1, float)
gui2_height_edit_m = pkg.addLabeledEdit(260 + 350, 70, "HMulti:", "1", 7, 1, float)
gui2_xstart_edit = pkg.addLabeledEdit(20 + 350, 110, "xstart:", "-3", 7, 1, float)
gui2_xend_edit = pkg.addLabeledEdit(100 + 350, 110, "xend:", "1", 7, 1, float)
gui2_ystart_edit = pkg.addLabeledEdit(180 + 350, 110, "ystart:", "-1.125", 7, 1, float)
gui2_yend_edit = pkg.addLabeledEdit(260 + 350, 110, "yend:", "1.125", 7, 1, float)
gui2_divide_edit = pkg.addLabeledEdit(20 + 350, 150, "delic:", "1", 7, 1, float)
gui2_xoff_edit = pkg.addLabeledEdit(100 + 350, 150, "xoff:", "0.0", 7, 1, float)
gui2_yoff_edit = pkg.addLabeledEdit(180 + 350, 150, "yoff:", "0.0", 7, 1, float)
gui2_iterations_edit = pkg.addLabeledEdit(260 + 350, 150, "iter:", "20", 7, 1, int)
gui2_percentage_lbl = pkg.addLabel(20 + 350, 230, "...")
gui2_generate_button = pkg.addButton(20 + 350, 190, "Generate", lambda: print("Not implemented"))


def generate_mandelbrot(directory="./", width=960, height=540, iterations=15, divider=1,
                        xoff=0, yoff=0, xstart=-3, xend=1, ystart=-1.125, yend=1.125, perc_lbl=gui_percentage_lbl):
    global dircnt, imgcnt
    global gui_percentage_lbl
    global pkg
    gui_percentage_lbl['text'] = "Awaiting..."
    pkg.wnd.update()
    jmc =  str(directory) + "/img_series_" + str(dircnt) + "/img_" + str(imgcnt) + ".bmp"

    imgref = imgpack(30, 300, jmc)
    imgref.makecanvas(width, height)

    xstart = xstart / divider
    xend = xend / divider
    ystart = ystart / divider
    yend = yend / divider
    xdist = dist(xstart, xend)
    ydist = dist(ystart, yend)

    for y in range(height):
        yp = (y / height)
        ypart = yp * ydist + yoff
        dst = int(yp * 100) + 1
        if dst % 4 == 0:
            gui_percentage_lbl['text'] = "%3.2f %%        " % dst
            pkg.wnd.update_idletasks()

        for x in range(width):
            xp = (x / width)
            xpart = xp * xdist + xoff

            z = complex(xstart + xpart, ystart + ypart)

            jmp = getIter(z, iterations)

            clr = (0, 0, 0)

            if not jmp % 2: clr = 64, 8, 32
            if not jmp % 3: clr = 0, 64, 32
            if not jmp % 4: clr = 8, 64, 128
            if not jmp % 5: clr = 16, 128, 0
            if not jmp % 6: clr = 192, 16, 192
            if not jmp % 7: clr = 16, 64, 255
            if not jmp % 8: clr = 64, 16, 64
            if not jmp % 9: clr = 16, 128, 128
            if not jmp % 10: clr = 64, 255, 16
            if jmp == iterations:
                clr = 0, 0, 0
            imgref.pixels[x, y] = clr

    imgref.save(directory)
    imgref.load(directory)




def generate_from_gui():
    divide = gui_divide_edit.value
    iterations = gui_iterations_edit.value
    filename = gui_filename_edit.value
    xstart = gui_xstart_edit.value
    xend = gui_xend_edit.value
    ystart = gui_ystart_edit.value
    yend = gui_yend_edit.value
    xoff = gui_xoff_edit.value
    yoff = gui_yoff_edit.value
    width = gui_width_edit.value
    height = gui_height_edit.value
    wm = gui_width_m_edit.value
    hm = gui_height_edit_m.value
    width = int(width * wm)
    height = int(height * hm)

    log("Values of elements")
    log(filename, width, height, xstart, xend,
        ystart, yend, iterations, divide,
        xoff, yoff)

    generate_mandelbrot(directory=filename,
                        width=width, height=height, iterations=iterations, divider=divide, xoff=xoff, yoff=yoff,
                        xstart=xstart, xend=xend, ystart=ystart, yend=yend, perc_lbl=gui2_percentage_lbl)




"""
for ii in range(8):
    part = 1 + ii/8

    for i in range(10):
        generate_mandelbrot(
                            width=int(960/4), height=int(540/4), iterations=i+1, divider=part)
"""

generate_from_gui()

pkg.wnd.update()
pkg.wnd.update_idletasks()
pkg.wnd.focus()

pkg.wnd.mainloop()
