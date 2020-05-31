import cv2
import imutils
from PIL import Image
import sys
from os import listdir
from os.path import isfile, join
import tempfile
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


### https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
### https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
### https://developer.ibm.com/technologies/python/tutorials/document-scanner
### https://gist.github.com/cancan101/80e27feaef8eae0ed921
### https://towardsdatascience.com/read-text-from-image-with-one-line-of-python-code-c22ede074cac
### https://github.com/tesseract-ocr/tesseract/wiki
### https://github.com/scott0123/Tesseract-macOS
### https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/


"""imS = cv2.resize(warped, (1350, 1150))
cv2.imshow("output", imS)
cv2.imwrite('Output Image.PNG', imS)
cv2.waitKey(0)"""

image_folder = "/Users/michael/Pictures/AmazonPhotos"


# workaround to load GIF with cv2
def load_gif(filename):
    img = Image.open(filename)

    with tempfile.NamedTemporaryFile(suffix=".png") as f:
        img.save(f.name)
        f.flush()
        src = cv2.imread(f.name)

    assert src is not None and len(src), "Empty"

    return src

# workaround to load GIF from URL with cv2
def load_gif_url(url):
    with tempfile.NamedTemporaryFile(suffix=".gif") as f:
        f.write(requests.get(url).content)
        f.flush()
        img = Image.open(f.name)

    with tempfile.NamedTemporaryFile(suffix=".png") as f:
        img.save(f.name)
        f.flush()
        src = cv2.imread(f.name)

    assert src is not None and len(src), "Empty"

    return src

def convert_pdf_to_png_image():
    """from wand.image import Image

    with Image(filename='sample_doc.pdf') as img:

        print('width =', img.width)
        print('height =', img.height)
        print('pages = ', len(img.sequence))
        print('resolution = ', img.resolution)

    with img.convert('png') as converted:
        converted.save(filename='sample_doc.png')"""
    return

# A bimodal image is an image in which most of the pixels are
# distributed over two dominant regions.
#
# cv2 has a method for OTSU binarization, which would work for bimodal
# images. It assumes the input intensities distribution to be bi-modal
# and tries to find the optimal threshold. Otsu binarization automatically
# calculates a threshold value from image histogram for a bimodal image.
def otsu_binarization():
    """img = cv2.imread("input_image.png", 0)
    ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
    print "Threshold selected : ", ret
    cv2.imwrite("./output_image.png", thresh)"""
    return

def cv2_imread(image_filepath):
    if image_filepath.endswith('.gif'):
        return load_gif(image_filepath)
    else:
        return cv2.imread(image_filepath)

def get_images(folder):
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    #print(onlyfiles)

    image_filepaths = []
    images = []
    for filename in onlyfiles:
        if not (filename.endswith('.gif') or filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.jpg')): continue
        image_filepath = join(folder, filename)
        image = cv2_imread(image_filepath)  # this can handle GIFs (as well as other image types)
        image_filepaths.append(image_filepath)
        images.append(image)
    
    return zip(image_filepaths, images)

def get_images_and_edges(folder, show_images=False):
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    #print(onlyfiles)

    image_filepaths = []
    images = []
    edged_images = []
    for filename in onlyfiles:
        if not (filename.endswith('.gif') or filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.jpg')): continue
        image_filepath = join(folder, filename)
        # load the image and compute the ratio of the old height
        # to the new height, clone it, and resize it
        #image = cv2.imread(image_filepath)
        image = cv2_imread(image_filepath)  # this can handle GIFs (as well as other image types)

        ratio = image.shape[0] / 500.0
        orig = image.copy()
        image = imutils.resize(image, height=500)

        # convert the image to grayscale, blur it, and find edges in the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5), 0)
        edged = cv2.Canny(gray, 75, 200)
        edged_images.append(edged)

        image_filepaths.append(image_filepath)
        images.append(image)

        if show_images:
            # show the original image and the edge detected image
            print("STEP 1: Edge Detection")
            cv2.imshow("Image", image)
            cv2.imshow("Edged", edged)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    return (image_filepaths, images, edged_images)


# The heuristic is this: we'll assume that the largest contour in the image
# with exactly four points is our piece of paper to be scanned.
#   edged is edge-detected version of the image
def find_paper_contours(orig, edged):
    screenCnt = None

    # find the contours in the edged image, keeping only the
    # largest ones, and initialize the screen contour
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break
    
    if screenCnt is None:
        print("...No countours found")
    else:
        # show the contour (outline) of the piece of paper
        print("STEP 2: Find contours of paper")
        cv2.drawContours(orig, [screenCnt], -1, (0, 255, 0), 2)
        cv2.imshow("Outline", orig)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


#(image_filepaths, images, edged_images) = get_images_and_edges(image_folder)
image_list = get_images(image_folder)

"""for (filepath, img, eimg) in zip(image_filepaths, images, edged_images):
    print(f"FILE: '{filepath}'")
    find_paper_contours(img, eimg)"""


for (filepath, img) in image_list:
    text = pytesseract.image_to_string(img)
    if text.strip() != "":
        print(f"FILE: '{filepath}'")
        output = text.replace('\n', ' ')
        print(f"{output}\n")


