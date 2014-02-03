import SimpleCV
import numpy as np
import scipy
def myconvolve(I, kernel):
    Inp = I.getGrayNumpy()
    rows = Inp.shape[0]
    cols = Inp.shape[1]
    d = kernel.shape[0]
    output=  np.zeros((rows, cols))
    Ipad = np.zeros((rows+d-1,cols+d-1))
    Ipad[d/2:rows-d/2+2, d/2:cols-d/2+2] = Inp
    kernel_ = np.fliplr(np.flipud(kernel))
    for i in range(d/2, rows-d/2+2):
        for j in range(d/2, cols-d/2+2):
            val = np.multiply(Ipad[i-d/2:i+d/2+1, j-d/2:j+d/2+1], kernel_).sum()
            if(val >= 255):
                val = 255
            if(val < 0):
                val = 0
            output[i-d/2, j-d/2] =val

    return SimpleCV.Image(output)

I = SimpleCV.Image("images/lena.jpg").grayscale()
#kernel = np.matrix([[ 1,  0, -1],[ 2,  0, -2],[ 1,  0,  1]])
kernel = np.matrix([[1,2,1],[0,0,0],[-1,-2,1]])
myconvolve(I, kernel).save("images/convolvemy.jpg")
scvCon = scipy.signal.convolve2d(I.getGrayNumpy(),kernel)
for i in range(0,I.width):
    for j in range(0, I.height):
        if scvCon[i,j] > 255:
            scvCon[i,j] = 255
        if scvCon[i,j] < 0:
            scvCon[i,j] = 0

SimpleCV.Image(scvCon).save("images/convolvescv.jpg")
a =raw_input("enter")
