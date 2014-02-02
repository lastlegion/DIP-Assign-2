import SimpleCV
import numpy as np

def mybitplane(I):
    bitplanes = np.zeros((8, I.width, I.height))
    Inp = I.getNumpy()[:,:,0]
    for i in range(0,8):
        bitplanes[i] = Inp&(2**i)
        Ii = SimpleCV.Image(bitplanes[i]).binarize()
        #bitplanes[i] = Ii.getNumpy()[:,:,0]/255
         
        bitplanes[i] = bitplanes[i]/2**i
        Ii.save("images/BitPlane"+str(i)+".jpg")
    return bitplanes

def reconstruct(bitplanes):
    Inp = np.zeros((bitplanes.shape[1], bitplanes.shape[2]))
    for i in range(0,8):
        Inp = Inp + (((bitplanes[i])*(2**i)))
        #Inp = Inp + bitplanes[i]
    return SimpleCV.Image(Inp)
              
def watermark(I,W):
    bitplanes = mybitplane(I)
    Inp = I.getNumpy()[:,:,0]
    Wnp = W.getNumpy()[:,:,0]
    for i in range(0,8):    #Watermark   
        Output = np.zeros((Inp.shape)) 
        for j in range(0,8):   
            if i == j: #Apply watermark
                Output = Output + ((Wnp/255)*2**i)
            else:
                Output = Output + bitplanes[j]*(2**j)
        SimpleCV.Image(Output).save("images/WatermarkLevel"+str(i)+".jpg");
    return Output

I = SimpleCV.Image("images/lena.jpg")
bitplanes = mybitplane(I)

R = reconstruct(bitplanes)
W = SimpleCV.Image("images/daiict.bmp")
WaterMark = watermark(I,W)
SimpleCV.Image(WaterMark).show()
R.show()
r=0
#r = raw_input("->")
print bitplanes
print R.getNumpy()
print bitplanes.shape
