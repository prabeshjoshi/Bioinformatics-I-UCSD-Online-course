import itertools
def hammingDistance(p,q):
    """ returns number of  mismatches in strings p and q"""
    misMatches = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            misMatches  +=1
    return misMatches        

def Neighbors(Pattern, d):
    x = ["A","G","C","T"]
    tups_list = list([p for p in itertools.product(x, repeat=10)])
    lst = []

    for i in tups_list:   
        st = ""
        for j in i:
            st+=j
        lst.append(st)   
    #return lst
    nbrs = []
    
    for i in lst:
        if hammingDistance(i,Pattern) <= d:
            nbrs.append(i)
    return nbrs
    


   
         
            