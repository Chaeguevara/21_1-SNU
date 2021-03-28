"""
Practical programming Chapter 10 Exercise 3

**Instruction**
All of the file-reading functions we have seen in this chapter read forward
through the file from the first character or line to the last. 
Complete P2 function that would read from the last line through a file 
and return a list whose elements are lines of the input file from the last.

For example, when you run P2 on alkaline_metals.txt (same text file as P1),
it should return 
['radium 88 226', 'barium 56 137.327\n', 'strontium 38 87.62\n', 'calcium 20 20.078\n', 'magnesium 12 24.305\n', 'beryllium 4 9.012\n']

"""

def P2(filename: str) -> list:        
    ##### Write your Code Here #####
    result = []
    #Read file
    with open(filename,'r') as file:
        lines = file.readlines()
        length = len(lines)
        for i in range(length,0,-1):
            line = lines[i-1]
            result.append(line)

    return result
    ##### End of your code #####
