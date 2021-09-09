import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import pytesseract


# Load image, grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('Page_1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Create rectangular structuring element and dilate
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
dilate = cv2.dilate(thresh, kernel, iterations=5)

# Find contours and draw rectangle
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]


line_items_coordinates = []

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
    #Here i ve to append each coordinate but the think is.. I can't Append 2 things a the same time
    #So may be it ll be better to crop it directly from here.

    #Here i ll take each crop of the boxe and i ll put in a list
    crop = image[y:y + h, x:x + w]
    #line_items_coordinates.append(crop)

    ret, thresh1 = cv2.threshold(crop, 120, 255, cv2.THRESH_BINARY)
    text = str(pytesseract.image_to_string(thresh1, config='--psm 6'))
    print(text)



    plt.imshow(Image.fromarray(crop))
    plt.show()
    im = Image.fromarray(image)



#Here i Can save my Marked Image
#One Problem is it is not Dynamic.. But not really important bc at the end we will not keep it
im.save('im.jpg')
print(type(im))



#Here i can directly with the list i did of the cropping make a visual of each crop //OCR



#Y en premier X en second Pour slice
#Le but ici c'est de save les coordonnées des rectangles fait
# (On catch de là le point en haut à gauchex,y ), la largeur et la hauteur.
# ca permettra d'avoir les 4 points

print(im.size)


#cv2.imshow('thresh', thresh)
#cv2.imshow('dilate', dilate)
#cv2.imshow('image', image)

print(line_items_coordinates)
cv2.waitKey()
