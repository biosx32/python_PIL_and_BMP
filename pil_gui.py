from pil_gui_extend import *

import os

# make time elapsed
# make time remaining
# make time expected



opt_filename = "E:\\test.bmp"
opt_width_m = 1
opt_height_m = 1
opt_width = 192*3
opt_height = 108*3
opt_xstart = -3
opt_xend = 1
opt_ystart = -1.125
opt_yend = 1.125
opt_divider = 100
opt_xoff = 0
opt_yoff = 0
opt_xoff_perc_b = 0
opt_yoff_perc_b = 0
opt_divider_perc = 0
opt_xoff_perc = 0
opt_yoff_perc = 0
opt_iterations = 10


gui_directory_edit = pkg.addLabeledEdit(20, 30, "Name:", opt_filename, 37, 0)
gui_width_edit = pkg.addLabeledEdit(20, 70, "Width:",opt_width , 7, 1, int)
gui_height_edit = pkg.addLabeledEdit(180, 70, "Height:", opt_height, 7, 1, int)
gui_width_m_edit = pkg.addLabeledEdit(100, 70, "WMulti:",opt_width_m , 7, 1, float)
gui_height_edit_m = pkg.addLabeledEdit(260, 70, "HMulti:", opt_height_m, 7, 1, float)
gui_xstart_edit = pkg.addLabeledEdit(20, 110, "xstart:", opt_xstart, 7, 1, float)
gui_xend_edit = pkg.addLabeledEdit(100, 110, "xend:", opt_xend, 7, 1, float)
gui_ystart_edit = pkg.addLabeledEdit(180, 110, "ystart:", opt_ystart, 7, 1, float)
gui_yend_edit = pkg.addLabeledEdit(260, 110, "yend:", opt_yend, 7, 1, float)
gui_divider_edit = pkg.addLabeledEdit(20, 150, "divider:", opt_divider, 7, 1, float)
gui_xoff_edit = pkg.addLabeledEdit(100, 150, "xoff:", opt_xoff, 7, 1, float)
gui_yoff_edit = pkg.addLabeledEdit(180, 150, "yoff:", opt_yoff, 7, 1, float)
gui_divider_perc_edit = pkg.addLabeledEdit(20, 190, "delic%", opt_divider_perc, 7, 1, float)
gui_xoff_perc_edit = pkg.addLabeledEdit(100  , 190, "xoff%->.:", opt_xoff_perc, 7, 1, float)
gui_yoff_perc_edit = pkg.addLabeledEdit(180  , 190, "yoff%->.:", opt_yoff_perc, 7, 1, float)
gui_xoff_perc_b_edit = pkg.addLabeledEdit(100  , 230, "xoff%->O:", opt_xoff_perc_b, 7, 1, float)
gui_yoff_perc_b_edit = pkg.addLabeledEdit(180  , 230, "yoff%->O:", opt_yoff_perc_b, 7, 1, float)
gui_iterations_edit = pkg.addLabeledEdit(260, 150, "iter:", opt_iterations, 7, 1, int)
gui_generate_button = pkg.addButton(20 , 250, "Generate", lambda: generate_from_gui())
gui_percentage_lbl = pkg.addLabel(20 , 280, "...")





def generate_mandelbrot(directory="./", width=opt_width, height=opt_height, iterations=opt_iterations, divider=opt_divider,
                        xstart=opt_xstart, xend=opt_xend,
                        ystart=opt_ystart, yend=opt_yend, xoff=opt_xoff, yoff=opt_yoff,
                        perc_lbl=gui_percentage_lbl,
                        xoff_perc=opt_xoff_perc, yoff_perc=opt_yoff_perc, xoff_perc_b=opt_xoff_perc_b,
                        yoff_perc_b = opt_yoff_perc_b):

    global dircnt, imgcnt
    global pkg
    divider /= 100
    xdist = dist(xstart, xend)
    ydist = dist(ystart, yend)



    print( *[ (x+"\t= "+str(y)) for x,y in
                dict(directory=directory,
                        width=width, height=height, iterations=iterations, divider=divider,
                        xstart=xstart, xend=xend, ystart=ystart, yend=yend,
                        xoff_perc_b=xoff_perc_b, yoff_perc_b=yoff_perc_b).items()
            ]
           ,
           sep='\n'
          )
    
    



    xoff_perc = xoff_perc * (xdist ) / 100
    xoff += xoff_perc

    xstart = xstart + xoff
    xend = xend + xoff

    yoff_perc = yoff_perc * (ydist ) / 100
    yoff += yoff_perc


    ystart = ystart + yoff
    yend = yend + yoff

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



    #LOOP

    for y in range(height):
        yp = (y / height)
        ypart = yp * ydist
        dst = int(yp * 100) + 1
        if dst % 4 == 0:
            perc_lbl['text'] = "%3.2f %%        " % dst
            pkg.wnd.update_idletasks()

        for x in range(width):
            xp = (x / width)
            xpart = xp * xdist

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
    divider = gui_divider_edit.value
    divider_perc = (gui_divider_perc_edit.value) * divider / 100
    divider += divider_perc
    xoff_perc_b = gui_xoff_perc_b_edit.value
    yoff_perc_b = gui_yoff_perc_b_edit.value


    iterations = gui_iterations_edit.value
    directory = gui_directory_edit.value
    xstart = gui_xstart_edit.value
    xend = gui_xend_edit.value
    ystart = gui_ystart_edit.value
    yend = gui_yend_edit.value



    xoff = gui_xoff_edit.value
    xdist = dist(xstart, xend)
    xoff_perc =  (gui_xoff_perc_edit.value) * (xdist/divider)
    xoff += xoff_perc
    xstart = xstart + xoff
    xend = xend + xoff
    yoff = gui_yoff_edit.value
    ydist = dist(ystart, yend)
    yoff_perc =  (gui_yoff_perc_edit.value) * (ydist/divider)
    yoff += yoff_perc
    ystart = ystart + yoff
    yend = yend + yoff
    width = gui_width_edit.value
    height = gui_height_edit.value
    wm = gui_width_m_edit.value
    hm = gui_height_edit_m.value
    width = int(width * wm)
    height = int(height * hm)

    

    log("Values of elements")
    log(directory, width, height, xstart, xend,
        ystart, yend, iterations, divider,
        xoff, yoff)

    generate_mandelbrot(directory=directory,
                        width=width, height=height, iterations=iterations, divider=divider,
                        xstart=xstart, xend=xend, ystart=ystart, yend=yend, perc_lbl=gui_percentage_lbl,
                        xoff_perc_b=xoff_perc_b, yoff_perc_b=yoff_perc_b)






for i in range(1,10+1): generate_mandelbrot(divider=25*i, xoff=-1.6)



pkg.wnd.update()
pkg.wnd.update_idletasks()
pkg.wnd.focus()

pkg.wnd.mainloop()
