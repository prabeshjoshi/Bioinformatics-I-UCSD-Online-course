#CODE CHALLENGE: Solve the Pattern Matching Problem.
#     Input: Two strings, Pattern and Genome.
#     Output: A collection of space-separated integers specifying all starting positions where Pattern appears
#     as a substring of Genome.


def find_pattern_position(pattern, genome):
    indices = [] 
    for i in range(len(genome) - len(pattern) -1):
        if genome[i:i+len(pattern)] == pattern:
            indices.append(i)
            
    list_to_string =  str(indices)
    return list_to_string.replace(",", "")
    
    
#read the sequence in a txt file and store it to variable genome"

#f = open('C:\Users\Prajwols\Downloads\dataset_4_5 (1).txt')

#genome = f.read()


#or       url = 'https://stepic.org/media/attachments/lessons/3/Vibrio_cholerae.txt'
#         genome = urllib2.urlopen(url).read()



         
            
        