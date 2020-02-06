import os, sys
from PIL import Image, ImageOps, ImageDraw

sizeA = 128, 128
sizeB = 64, 64

def crop_circle(filename, size):
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + size, fill=255)
    im = Image.open(filename)
    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save(filename)
    return

def crop_square(filename, size):
    print filename
    img = Image.open(filename)

    width = img.size[0]
    height = img.size[1]
    min_dim = min(width, height)
    half_min = min_dim / 2
    half_the_width = half_min
    half_the_height = half_min
    img_square = img.crop(
        (
            half_the_width - half_min,
            half_the_height - half_min,
            half_the_width + half_min,
            half_the_height + half_min
        )
    )
    img_square.thumbnail(sizeA, Image.ANTIALIAS)
    return img_square
    
def create_thumbnail(infile):
    outfileA = os.path.splitext(infile)[0] + ".thumbnail.A.png"
    outfileB = os.path.splitext(infile)[0] + ".thumbnail.B.png"
    if infile != outfileA and infile != outfileB:
        try:
            img_square = crop_square(infile, sizeA)
            img_square.save(outfileA, "PNG")
            img_square = crop_square(infile, sizeB)
            img_square.save(outfileB, "PNG")
            crop_circle(outfileA, sizeA)
            crop_circle(outfileB, sizeB)
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
    return

################################################################################

path = r"D:\Users\mhatmaker\Dropbox\MyProjects\CoronaProjects\AudioRecorder\faces"

count = 14
for i in range(1, count+1):
    filename = "face{0:04d}.jpg".format(i)
    #script_path = os.path.dirname(os.path.realpath(__file__))
    #pathname = os.path.join(script_path, filename)
    pathname = os.path.join(path, filename)    
    create_thumbnail(pathname)

