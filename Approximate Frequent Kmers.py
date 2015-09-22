def hammingDistance(p,q):
    """ returns number of  mismatches in strings p and q"""
    misMatches = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            misMatches  +=1
    return misMatches        
   
 
def approx_occurrences(pattern, text, d):
    """Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
     Input: Strings Pattern and Text along with an integer d.
     Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches."""
    patternLen = len(pattern)
    start_pos = []
    for i in range(len(text)-patternLen+1):
        if hammingDistance(text[i:i+patternLen] ,pattern) <= d:
            start_pos.append(i)
    return start_pos
    
  
  
        
def countD(pattern, text, d):
    return len(approx_occurrences(pattern, text, d))
    
 

        
def approx_frequent_words(text,k,d):
    count = []
    for i in range(len(text)- k+1):
        pattern = text[i:i+k]
        count.append(countD(pattern, text, d))
        
    max_count = max(count)
    frequent_patterns = []
    
    for i in range(len(text)- k+1):
        if count[i] == max_count:
            frequent_patterns.append(text[i:i+k])
            
    unique = list(set(frequent_patterns))

    #return unique   ## if needed 
    return (frequent_patterns)
        
            
