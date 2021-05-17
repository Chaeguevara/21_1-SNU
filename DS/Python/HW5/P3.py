"""
**Instruction**
Write P3 function that reads a file and return a list of lines except header(any line starts with '//').
Also exclude new lne character('\n') and any commented part.(marked as '#')
If any line starts with comment mark('#'), ignore the line.

For example, if the input file has below lines, 

//Header: description
//metals no weight
beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078 #Good for your health
strontium 38 87.62
barium 56 137.327
# This is comment line and  ignore
radium 88 226


P3 should return below list.
['beryllium 4 9.012', 'magnesium 12 24.305', 'calcium 20 20.078 ', 'strontium 38 87.62', 'barium 56 137.327', 'radium 88 226']

"""

def P3(filename: str) -> list:        
    ##### Write your Code Here #####    
    result = []
    # Read file
    with open(filename,'r') as file:
        lines = file.readlines()
        #for lines, if it starts with '#/' -> skip
        for line in lines:
            if line.startswith("#") or line.startswith("/"):
                pass 
            else:
            #for lines try split # and if true, select line[0]
                sub_result = line.split('#')[0]
                sub_result = sub_result.replace('\n','')
                result.append(sub_result)
    return result
    ##### End of your code #####

print(
    P3("alkain_2.txt")
)