import SimpleCV
import numpy as np

I = SimpleCV.Image("images/1small.jpg")

Inp = I.getGrayNumpy()

X= np.zeros((9,3))
count=0
for i in range(-1,2):
    for j in range(-1,2):
        X[count] = np.matrix([1,i,j])
        count=count+1
F = Inp[0:3,0:3].reshape(9,1)
print X
print F
res = np.linalg.lstsq(X,F)
print res
a = res[0][0][0]
b = res[0][1][0]
c = res[0][2][0]
mask = np.zeros((3,3))
print a,b,c
Xi = np.linalg.pinv(X)
Mask1 = Xi[0]
Mask2 = Xi[1]
Mask3 = Xi[2]
print Mask1
print Mask2
print Mask3

'''
for i in range(-1,1):
    for j in range(-1,1):
        mask[i+1,j+1] = a*1 +b*i + c*j
print mask
'''
