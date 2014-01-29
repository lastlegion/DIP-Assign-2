import SimpleCV
import numpy as np

def mybitplane(I):
    bitplanes = np.zeros((8, I.width, I.height))
    Inp = I.getNumpy()[:,:,0]
    for i in range(0,8):
        bitplanes[i] = Inp&(2**i)
        Ii = SimpleCV.Image(bitplanes[i])
        Ii.save("images/BitPlane"+str(i)+".jpg")
    return bitplanes
I = SimpleCV.Image("images/1small.jpg")
mybitplane(I)
        

