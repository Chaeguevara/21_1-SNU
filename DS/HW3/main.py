#!/usr/bin/env python3

from P1 import P1
from P2 import P2
from P3 import P3
from P4 import P4
from P5 import P5
from P6 import P6
from P7 import P7
from P8 import P8
from P9 import P9
from P10 import P10

def main():
    test_P1()
    test_P2()
    test_P3()
    test_P4()
    test_P5()
    test_P6()
    test_P7()
    test_P8()
    test_P9()
    test_P10()

def test_P1():
    # Test P1
    input1 = [[3, 4, 2, 8, 3], ['apple', 'banana', 'pear'],[4.0, 4.5]]
    output = [True, False, False]
    test_one_fn(P1, input1, output)

def test_P2():
    input1 = [[1, 2, 3], ['abcdef'], ['a', 'b', 'c']]
    input2 = [[4, 5],['ab', 'cd', 'ef'],[1, 2, 3]]
    output = [True, False, False]
    test_two_fn(P2, input1, input2, output)

def test_P3():
    input1 = [[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3], [0,0,0]]
    output = [[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4], [1,1,1]]
    test_one_fn(P3, input1, output)

def test_P4():
    input1=[2,0]
    input2=[22,100]
    output=[12,50]
    test_two_fn(P4,input1,input2,output)

def test_P5():
    input1 = [[1,2,3,-3,6,-1,-3,1], [-5, 1, -3, 2]]
    output = [[1, 2, 3, 6, 1],[1, 2]]
    test_one_fn(P5, input1,output)

def test_P6():
    input1 = [[4353, 2314, 2956, 3382, 9362, 3900]]
    output = [[1830, 2314, 2956, 3900, 4353, 5566, 9362]]
    test_one_fn(P6, input1,output)

def test_P7():
    input1 = [[['km','miles','league'],['kg','pound','stone']], [[0,1,2,3],[4,5,6]], [[0,0,0],[1]]]
    output = [['km','stone'],[0,6],[0,1]]  
    test_one_fn(P7,input1,output)

def test_P8():
    input1= [1,3,5]
    output = [False,True,False]

    rat_1 = [5, 6, 7, 6, 7, 8, 10, 9, 8, 10]
    rat_2 = [7, 8, 6, 7, 8, 10, 9, 8, 10, 11]
    for inp1, out in zip(input1,output):
        result = P8(rat_1,rat_2,inp1)
        assert result == out, f'Failed at {fn} \ninput: {inp1} expected output: {out} \nbut received {result}'

def test_P9():
    input1 = [[5, 6, 7, 6, 7, 8, 10, 9, 8, 10], [5, 6, 7, 6, 7]]
    input2 = [[7, 8, 6, 7, 8, 10, 9, 8, 10, 11],[7, 8, 6, 7, 8]]
    output = [[5, 7, 6, 8, 7, 6, 6, 7, 7, 8, 8, 10, 10, 9, 9, 8, 8, 10, 10, 11], [5, 7, 6, 8, 7, 6, 6, 7, 7, 8]]
    test_two_fn(P9, input1,input2, output)

def test_P10():
    input1 = [33,-10,10]
    input2 = [49,-7,11]
    output = [[33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49],[-10, -9, -8, -7],[10, 11]]
    test_two_fn(P10, input1,input2,output)

def test_one_fn(fn, inputs, outputs):
    for inp,outp in zip(inputs,outputs):
        result = fn(inp)
        assert result == outp, f'Failed at {fn} \ninput: {inp} expected output: {outp} \nbut received {result}'

def test_two_fn(fn, input1, input2, outputs):
    for inp1, inp2, outp in zip(input1, input2, outputs):
        result = fn(inp1,inp2)
        assert result == outp, f'Failed at {fn} \ninput: {(inp1, inp2)} expected output: {outp} \nbut received {result}'


if __name__ == '__main__':
    main()