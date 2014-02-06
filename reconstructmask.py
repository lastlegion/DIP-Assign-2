import SimpleCV
import numpy as np

def pointwise(Mat1, Mat2):
    Matr = np.zeros(Mat1.shape)
    for i in range(0, Mat1.shape[0]):
        for j in range(0, Mat1.shape[1]):
            Matr[i,j] = Mat1[i,j]*Mat2[i,j]
    return Matr
def findabc(Inp, X):

    F = Inp[0:3,0:3].reshape(9,1)
#    print X
#    print F
    res = np.linalg.lstsq(X,F)
#    print res
    a = res[0][0][0]
    b = res[0][1][0]
    c = res[0][2][0]
    mask = np.zeros((3,3))
    print a,b,c


I = SimpleCV.Image("images/lena.jpg")

Inp = I.getGrayNumpy()
X= np.zeros((9,3))
count=0
for i in range(-1,2):
    for j in range(-1,2):
        X[count] = np.matrix([1,i,j])
        count=count+1

findabc(Inp,X)

Xi = np.linalg.pinv(X)
Mask1 = np.array(Xi[0].reshape(3,3))
Mask2 = np.array(Xi[1].reshape(3,3))
Mask3 = np.array(Xi[2].reshape(3,3))
print np.around(Mask1,1)
print np.around(Mask2,1)
print np.around(Mask3,1)

w  = np.matrix([[1,2,1],[2,4,2],[1,2,1]])
#Maskw1 = np.array(Xi[0].reshape(3,3)*w)
#Maskw2 = np.array(Xi[1].reshape(3,3)*w)
#Maskw3 = np.array(Xi[2].reshape(3,3)*w)
Maskw1 = np.array(pointwise(Xi[0].reshape(3,3), w))
Maskw2 = np.array(pointwise(Xi[1].reshape(3,3), w))
Maskw3 = np.array(pointwise(Xi[2].reshape(3,3), w))
print np.around(Maskw1,1)
print np.around(Maskw2,2)
print np.around(Maskw3,3)

print Mask1.shape
I1 = I.convolve(Mask1).save("images/conv1.jpg")
I2 = I.convolve(Mask2).save("images/conv2.jpg")
I3 = I.convolve(Mask3).save("images/conv3.jpg")
Iw1 = I.convolve(Maskw1).save("images/convw1.jpg")
Iw2 = I.convolve(Maskw2).save("images/convw2.jpg")
Iw3 = I.convolve(Maskw3).save("images/convw3.jpg")


'''
for i in range(-1,1):
    for j in range(-1,1):
        mask[i+1,j+1] = a*1 +b*i + c*j
print mask
'''
