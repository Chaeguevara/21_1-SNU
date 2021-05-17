"""
Practical programming Chapter 10 Exercise 2

**Instruction**
Suppose the file alkaline_metals.txt contains the name, atomic number, and
atomic weight of the alkaline earth metals:

beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078
strontium 38 87.62
barium 56 137.327
radium 88 226

Complete P1 function that uses a for loop to read the contents of alkaline_metals.txt and store it in a list
of lists, with each inner list containing the name, atomic number, and atomic weight for an element. (Do not include new line character('\n'))
Then return the list of lists.


"""
def P1(filename: str) -> list:        
    result = []
    # Read file
    with open(filename,'r') as file:
    
        lines = file.readlines()
        
        #Loop through each line
        for line in lines:
            line = line.replace("\n","")
            sub = line.split(" ")
            result.append(sub)
    print(result)

    return result
    ##### End of your code #####
