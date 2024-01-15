import numpy as np
import cv2

file = open(r'demofile.txt','r')

string = file.read()
i = 0
arr = []
for itr in string:
    num = ord(itr)
    arr.insert(i,str(format(num,'08b')))
    i += 1



#print(arr)

final_img = np.ones((10,1920,3),dtype = np.uint8)  #needs a better way
final_img = final_img * 255

img1 = np.ones((10,10,3),dtype = np.uint8)  #needs a better way
img1 = img1 * 255

row = 0
column = 0
filename_itr = 0
filename = 'photo{}.png'

for y in arr:
    for x in y:
        if x == '0':
            img = np.zeros((10,10,3),dtype = np.uint8)
            img = 255*img
        else:
            img = np.ones((10,10,3),dtype = np.uint8)
            img = 255*img
        img1 = np.hstack((img1,img))
        column += 10
    if(column == 1920):
        img1 = np.delete(img1,np.s_[:10],1)
        final_img = np.vstack((final_img,img1))
        row += 10
        img1 = np.ones((10,10,3),dtype = np.uint8)  #needs a better way
        img1 = img1 * 255
        column = 0

    if(row == 1080):
        print('printing photo', filename_itr)
        final_img = np.delete(final_img,np.s_[:10],0)
        cv2.imwrite(filename.format(filename_itr),final_img)
        filename_itr += 1
        img1 = np.ones((10,10,3),dtype = np.uint8)  #needs a better way
        img1 = img1 * 255
        final_img = np.ones((10,1920,3),dtype = np.uint8)  #needs a better way
        final_img = final_img * 255
        row = 0
        column = 0

print('printing photo', filename_itr)
print(column)
print(row)


final_img = np.delete(final_img,np.s_[:10],0)
img1 = np.delete(img1,np.s_[:10],1)

grey_img = np.ones((10,(1920-column),3),dtype = np.uint8)  #needs a better way
grey_img = grey_img * 127

img1 = np.hstack((img1,grey_img))
final_img = np.vstack((final_img,img1))

grey_img = np.ones(((1080-row),1920,3),dtype = np.uint8)  #needs a better way
grey_img = grey_img * 127

final_img = np.vstack((final_img,grey_img))

cv2.imwrite(filename.format(filename_itr),final_img)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mov', fourcc, 1.0, (1920,1080))

for x in range (0, (filename_itr + 1)):
    print('using photo - ', filename.format(x))
    img = cv2.imread(filename.format(x))
    #print(img)
    #cv2.imshow("Frame", img)
    #key = cv2.waitKey(0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #cv2.imshow("Frame", img)
    #key = cv2.waitKey(0)
    out.write(img)
#out.write(img)
#file.release()
out.release()
