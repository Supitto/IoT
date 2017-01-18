import numpy
from PIL import Image

# Specify image width and height
w, h = 200, 200
 
# Specify real and imaginary range of image
re_min, re_max = -2.0, 2.0
im_min, im_max = -2.0, 2.0
 
# Generate evenly spaced values over real and imaginary ranges
real_range = numpy.arange(re_min, re_max, (re_max - re_min) / w)
imag_range = numpy.arange(im_max, im_min, (im_min - im_max) / h)

imagem = Image.new('L',(w,h))
pixel = imagem.load()

def fractal(val):
    c = complex(0.0,val)
    h = 200
    for im in imag_range:
        w=200
        for re in real_range:
            z = complex(re, im)
            n = 255
            while abs(z) < 10 and n >= 5:
                z = z*z + c
                n -= 5
            # Write pixel to file
            pixel[200-w,200-h] = (n)
            w-=1
        h-=1
    return imagem
