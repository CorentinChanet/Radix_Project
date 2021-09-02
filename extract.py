from pdf2image import convert_from_path

pdfs = "../pdf/1.pdf"
pages = convert_from_path(pdfs, 350)

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i = i+1


import cv2
from PIL import Image


"""def mark_region(image_path):

    im = cv2.imread(image_path)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9,9), 0)
    thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)

    # Dilate to combine adjacent text contours
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
    dilate = cv2.dilate(thresh, kernel, iterations=4)

    # Find contours, highlight text areas, and extract ROIs
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    line_items_coordinates = []

    count = 0
    for c in cnts:
        area = cv2.contourArea(c)
        x,y,w,h = cv2.boundingRect(c)

        print(str(count)+'x'+str(x))
        print(str(count)+'y'+str(y))
        print(str(count)+'w'+str(w))
        print(str(count)+'h'+str(h))
        count+=1

        if y >= 200 and x <= 1000:
            if area > 10000:
                image = cv2.rectangle(im, (x,y), (x+w, y+h), color=(2,0,255), thickness=10)
                line_items_coordinates.append([(x,y), (2200, y+h)])

        if y >= 2400 and x<= 500:
            image = cv2.rectangle(im, (x,y), (2200, y+h), color=(255,0,255), thickness=6)
            line_items_coordinates.append([(x,y), (3000, y+h)])



    return image, line_items_coordinates

image = Image.fromarray(mark_region('Page_1.jpg')[0])

image.show()"""
#mark_region('Page_1.jpg')