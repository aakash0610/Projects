import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("2.jpg")
cv2.cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Detecting words
height_img, width_img, _ = img.shape
box = pytesseract.image_to_data(img)
#here we use enumarate for counter, instead of having a variable count and adding it in a loop.

for x,b in enumerate(box.splitlines()):

    #here we use x to keep a count and as we need to omit the 0th line as it is unecessery here.

    if x!=0:
        b = b.split()
        print(b)
        #here len(b) == 12 is specified as whenever there is a word present in the list there are 12 number of values created.
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,  y), (w+x, h+y), (0, 0, 255), 1)
            cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)



cv2.imshow("Img", img)
cv2.waitKey(0)
