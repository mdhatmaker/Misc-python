from cv2 import imread, cvtColor, COLOR_BGR2GRAY, imshow, waitKey

# https://github.com/TheAlgorithms/Python

if __name__ == '__main__':
    # read original image
    img = imread('lena.jpg')
    img = imread('../image_data/lena.jpg')
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)
