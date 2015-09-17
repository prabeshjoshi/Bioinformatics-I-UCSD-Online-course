import itertools
def SeqToNumDict(k):
    
    x = ["A","G","C","T"]
    tups_list = list([p for p in itertools.product(x, repeat=k)])
    lst = []

    for i in tups_list:   
        st = ""
        for j in i:
            st+=j
        lst.append(st)   
        
        mapping= {}    
    for i in range(len(lst)):
             mapping[lst[i]] = i
             
    return mapping  

def NumToSeqDict(k):
    
    x = ["A","G","C","T"]
    tups_list = list([p for p in itertools.product(x, repeat=k)])
    lst = []

    for i in tups_list:   
        st = ""
        for j in i:
            st+=j
        lst.append(st)   
        
        mapping= {}    
    for i in range(len(lst)):
             mapping[i] = lst[i]
             
    return mapping  
    
def seqtoNums(seq,k):
    mapp = SeqToNumDict(k)  
    seqOfNums = []
    for i in range(len(seq)-k):
        seqOfNums.append(mapp[seq[i:i+k]])
    return seqOfNums    

def NumToSeq(seq,k):
    mapp = NumToSeqDict(k)  
    seqOfNums = []
    for i in range(len(seq)):
        seqOfNums.append(mapp[seq[i]])
    return seqOfNums    
