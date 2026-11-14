import cv2
import os
img = cv2.imread(r"C:\Users\vijay\OneDrive\Desktop\OPEN CV\Save_IMG'S\random-ai-generated-images.png")
cv2.imshow("Title",img)
cv2.waitKey(0)
img1 = cv2.imread(r"C:\Users\vijay\OneDrive\Desktop\OPEN CV\Save_IMG'S\random-ai-generated-images.png",0)
cv2.imshow("Title",img1)
cv2.waitKey(10000)
PATH_FOLDER = r"C:\Users\vijay\OneDrive\Desktop\OPEN CV\Save_IMG'S"
os.chdir(PATH_FOLDER)
cv2.imwrite("Grayscale Image.jpg",img1)