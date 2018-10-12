import cv2 #importing openCV library
import matplotlib.pyplot as plt #importing a function from mpl
import tkinter as tk #GUI help from tkinter for filedialog to select files in windows
from tkinter import filedialog


name=input("Name?")

root=tk.Tk()
root.withdraw() #to avoid root windows of tkinter
path=filedialog.askopenfilename() #taking in file and storing the path
bgr_img=cv2.imread(path) #reading the file
gray_img=cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)#converting
cv2.imwrite('converted.jpg',gray_img)#storing
print("Hello " +name +", Your file is being converted......")

plt.imshow(gray_img,cmap=plt.get_cmap('gray'))
plt.xticks([]),plt.yticks([])#hide ticks on x and y axis
plt.show()


