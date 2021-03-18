from P10 import P10
from P9 import P9
from P8 import P8
from P7 import P7
from P6 import P6
from P4 import P4
from P3 import P3
from P2 import P2
from P1 import P1

p1_l1 = [3, 4, 2, 8, 3]
p1_l2 = ['apple', 'banana', 'pear']
p1_l3 = [4.0, 4.5]
pl_l4 = ['apple', 'Apple']
pl_l5 = ['True', True]
print("----Test P1 Starts----")
print("Expected:True \t Actual:",P1(p1_l1))
print("Expected:False \t Actual:",P1(p1_l2))
print("Expected:False \t Actual:",P1(p1_l3))
print("Expected:False \t Actual:",P1(pl_l4))
print("Expected:False \t Actual:",P1(pl_l5))
print("----Test P1 Ends----\n")


p2_l1_1 = [1, 2, 3]
p2_l1_2 = [4, 5]
p2_l2_1 = ['abcdef']
p2_l2_2 = ['ab', 'cd', 'ef']
p2_l3_1 = ['a', 'b', 'c']
p2_l3_2 = [1, 2, 3]
print("----Test P2 Starts----")
print("Expected:True \t Actual:",P2(p2_l1_1, p2_l1_2))
print("Expected:False \t Actual:",P2(p2_l2_1, p2_l2_2))
print("Expected:False \t Actual:",P2(p2_l3_1, p2_l3_2))
print("----Test P2 Ends----\n")

p3_l1 = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
p3_l2 = [0, 0, 0]
p3_l3 = []
print("----Test P3 Starts----")
print("Expected:[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4] \t Actual:",P3(p3_l1))
print("Expected:[1, 1, 1] \t Actual:",P3(p3_l2))
print(P3(p3_l3))
print(P3("p3_l3"))
print("----Test P3 Ends----\n")

print("----Test P4 Starts----")
print(P4(2, 22))
print(P4(0, 100))
print(P4(1, 1))
print("----Test P4 Ends----\n")

print("----Test P6 Starts----")
print(P6([4353, 2314, 2956, 3382, 9362, 3900]))
print(P6([423676, 23512, 3382, 786, 2964, 4505]))
print("----Test P6 Ends----\n")

print("----Test P7 Starts----")
print(P7([['km', 'miles', 'league'], ['kg', 'pound', 'stone']]))
print(P7([[0, 1, 2, 3], [4, 5, 6]]))
print("----Test P7 Ends----\n")

print("----Test P8 Starts----")
rat_1 = [5, 6, 7, 6, 7, 8, 10, 9, 8, 10]
rat_2 = [7, 8, 6, 7, 8, 10, 9, 8, 10, 11]
print(P8(rat_1, rat_2, 5))
print(P8(rat_1, rat_2, 6))
print(P8(rat_1, rat_2, 3))
print("----Test P8 Ends----\n")

rat_3 = [1, 5, 7, 3, 8, 0, 5, 10, 12]
rat_4 = [77, 85, 96, 36, 53, 17, 35, 12, 49]
print("----Test P9 Starts----")
print(P9(rat_1, rat_2))
print(P9(rat_3, rat_4))
print("----Test P9 Ends----\n")

print("----Test P10 Starts----")
print(P10(33, 49))
print(P10(-10, -7))
print(P10(10, 11))
print("----Test P10 Ends----\n")
