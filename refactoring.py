import numpy as np
import cv2

def word2image(word):
    img1 = np.ones((50,50,3),dtype = np.uint8)  #needs a better way
    img1 = img1 * 255
    for x in word:
        if x == '0':
            img = np.zeros((50,50,3),dtype = np.uint8)
            img = 255*img
        else:
            img = np.ones((50,50,3),dtype = np.uint8)
            img = 255*img
        img1 = np.hstack((img1,img))
    img1 = np.delete(img1,np.s_[:50],1)
    return img1

string = 'My name is \"Akash Sinha\"'
i = 0
arr = []
for itr in string:
    num = ord(itr)
    arr.insert(i,str(format(num,'08b')))
    i += 1

print(arr[0])

img1 = word2image(arr[0])
cv2.imshow('black image', img1)
cv2.waitKey(0)
