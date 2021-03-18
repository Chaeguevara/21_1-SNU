"""
Practical programming Chapter 9 Exercise 8

**Instruction**
You are given two lists, rat_1 and rat_2, that contain the daily weights of
two rats.  
Complete P9 function to return output_list as following:
  the first element of output_list is the first element of rat_1
  the second element of output_list is the first element of rat_2
  the third element of output_list is the second element of rat_1
  the fourth element of output_list is the second element of rat_2
  the 5th element of output_list is the third element of rat_1
  the 6th element of output_list is the third element of rat_2
  ...
Assume the length of rat_1 is equal to the length of rat_2

rat_1 = [5, 6, 7, 6, 7, 8, 10, 9, 8, 10]
rat_2 = [7, 8, 6, 7, 8, 10, 9, 8, 10, 11]

P9(rat_1, rat_2)
>>> [5, 7, 6, 8, 7, 6, 6, 7, 7, 8, 8, 10, 10, 9, 9, 8, 8, 10, 10, 11]
    

rat_1 = [5, 6, 7, 6, 7]
rat_2 = [7, 8, 6, 7, 8]
P9(rat_1, rat_2)
>>> [5, 7, 6, 8, 7, 6, 6, 7, 7, 8]

"""


def P9(rat_1: list, rat_2: list) -> list:
    ##### Modify code Here #####
    result = []

    # Basic rule
    # Append the elements in turn one by one
    # when going through iteration, if the i is even number, append from rat_1 otherwise from rat_2
    # double the size of the loop
    for i in range(len(rat_1)*2):
      if i%2 == 0:
        result.append(rat_1[i//2])
      else:
        result.append(rat_2[i//2])
    return result
    ##### End of your code #####