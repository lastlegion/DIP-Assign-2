import SimpleCV
import numpy as np

def myhisteq(I=SimpleCV.Image("images/lena.jpg"), N=10):
    
    Inp = I.getNumpy()    
    bin_range = 255/N
    hist = np.zeros((N))
    prob = np.zeros((N))
    for i in range(0, I.width):
        for j in range(0, I.height):
            binid = min(Inp[i,j][0]/bin_range, N-1)
            hist[binid] = hist[binid]+1
            prob[binid] = hist[binid]/I.area()
    print hist
    print prob
    Ieq = np.zeros((I.width, I.height))
    eqprob = np.zeros((N))
    for i in range(0, I.width):
        for j in range(0, I.height):
            binid = min(Inp[i,j][0]/bin_range, N-1)
            T = 0
            for r in range(0, binid+1):
                T = T+ (255)*prob[r]
            Ieq[i,j] = T
    SimpleCV.Image(Ieq).show()
    return SimpleCV.Image(Ieq)

I = SimpleCV.Image("images/1small.jpg")
N=255
myhisteq()
myhisteq(I,N).save("images/histeq-my.jpg")
I.equalize().save("images/histeq-scv.jpg")
