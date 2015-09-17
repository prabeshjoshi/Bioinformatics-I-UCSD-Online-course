#     """ PatternCount(Text, Pattern)
 #       count ← 0
  #      for i ← 0 to |Text| − |Pattern|
   #         if Text(i, |Pattern|) = Pattern
    #            count ← count + 1
     #   return count"""


import sys
lines = sys.stdin.read().splitlines() # read in the input from STDIN
Text = lines[0]
Pattern = lines[1]

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count


print(PatternCount(Text,Pattern))
