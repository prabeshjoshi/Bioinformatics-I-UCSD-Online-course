f = open('C:\Users\Prajwols\Downloads\dataset_7_6.txt','r')     
seq = f.readline().strip()


def skewGC(seq):
    """Returns G - C from the start (0) position to end"""
    c=0
    g=0
    out = [0]
    temp = 0
    for nt in seq:
        if nt =="C":
            c+= 1
        elif nt == "G":
            g+=1
            
        out.append(g-c)
        
    return out

print skewGC(seq)


import pylab

f = open('C:\Users\Prajwols\Desktop\Bioinformatcs I\Vibrio_cholerae.txt','r')     # file from week 1 
genome = f.readline().strip()
answer = skewGC(genome)
array = []
for num in answer:
    array.append(num)
pylab.plot(array)
#pylab.show()

f.close()
 





def minPos(seq):
    """returns the positions with minimum G-C values"""
    temp = 0
    pos = 0
    g= 0
    c=0
    minPos = []
    for nt in seq:
        if nt =="C":
            c+= 1
        elif nt == "G":
            g+=1
        temp =  g-c    
        pos += 1
        if temp == minVal:
            minPos.append(pos)
            
    return minPos    


minVal = min(skewGC(seq))
        
print minPos(seq)

        
