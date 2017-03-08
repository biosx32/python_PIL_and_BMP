from PIL import Image

v=10
xsize = 700*v
ysize = 700*v
itr = 20
img = Image.new('RGB', (xsize, ysize), "black")
pixels = img.load()

ystart = -2
yend = 4 - abs(ystart)
xstart = -2.5
xend = 4 - abs(xstart)







def dist(x,y):
    if x>y:
        x,y = y,x

    return y - x


xdist = dist(xstart, xend)
ydist = dist(ystart, yend)

z = complex(0,0)


def getIter(z):
    c = z
    for iteration in range(itr):
        z = z ** 2 + c
        if abs(z) >= 2:
            return iteration + 1
    return None

for y in range(ysize):
    ypart = (y / ysize) * ydist
    for x in range(xsize):
        xpart = (x / xsize) * xdist
        z = complex(xstart + xpart, ystart + ypart)

        jmp = getIter(z)


        if jmp is None:
            pixels[x, y] = (0, 0, 0)

        else:
            pixels[x, y] = (255,255,255)





img.show()

