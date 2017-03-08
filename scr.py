import sys

arg = False 


printf = lambda *a, **kw: print(*a, end='',sep=(' ' if ('sep' not in kw.keys()) else kw['sep']))


if len(sys.argv) - 1:
	arg = sys.argv[1]

a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0

def main(arg):
	if not arg:
		full = input("Zadaj segment: ")
	else:
		full = arg
	if not full:
		full = "10101010"
	print(full)
	for char in full:
		if char not in "01":
			full.replace(char, "")

	full = full.replace("0", ":")
	full = full.replace("1", "\u2588")
	full = full[::-1]
	a,b,c,d,e,f,g,h = tuple(full)

	print()
	a1 = " {sep}{a}\n".format(a=a*16, sep=' '*5)
	b1 = "  {f}{sep}{b}\n".format(f=f*4, b=b*4, sep=' '*16)
	c1 = " {sep}{g}\n".format(g=g*16, sep=' '*5)
	d1 = "  {e}{sep}{c}\n".format(e=e*4, c=c*4, sep=' '*16)
	e1 = " {sep}{d}\n".format(d=d*16, sep=' '*5)

	h1 = "{sep}{h}\n".format(h=h*7, sep=' '*32)

	printf(a1*2)
	printf(b1*6)
	printf(c1*2)
	printf(d1*6)
	printf(e1*2)
	printf(h1*3)

main(arg)

if 0:
	from time import sleep
	for img_i in range(256):
		a=str(bin(img_i)) \
			.replace("0b", "") \
			.zfill(8)
		print(a)
		main(a)
		sleep(0.5)
