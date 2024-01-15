import cv2
import numpy as np
import math

def toString(a):
    l=[]
    m=""
    for i in a:
        i = int(i)
        b=0
        c=0
        k=int(math.log10(i))+1
        for j in range(k):
            b=((i%10)*(2**j))
            i=i//10
            c=c+b
        l.append(c)
    for x in l:
        m=m+chr(x)
    return m


cap = cv2.VideoCapture(r'output.avi')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )
cv2.namedWindow("Frame")
while(cap.isOpened()):
    _, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    npdata = np.asarray(image)
    column = 5
    row = 5
    str = ''
    width  = cap.get(3)  # float `width`
    height = cap.get(4)
#    print(width,' ',height)
    for y in range(1,109):
        for x in range(1,193):
            if(npdata[row][column][0] <= 25):
                str = str + '0'
            elif(npdata[row][column][0] >= 230):
                str = str + '1'
            else:
                break
            column += 10
        column = 5
        row += 10
    arr = []
    print(int(len(str)/8))
    for x in range(0,int(len(str)/8)):
        arr.insert(x,str[:8])
        str = str[8:]

#    print(len(arr))
#    print(arr)
    print(toString(arr))
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key == 27:
         break

cap.release()
cv2.destroyAllWindows()
