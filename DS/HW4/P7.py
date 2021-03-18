"""
Implement a function that takes a dictionary of dictionaries in the format 
described in the previous question(P6) and returns True
if and only if every one of the inner dictionaries has exactly the same keys.

* Condition 1: There is no case where the value of value is dictionary or the value of value of value is dictionary ... so on)
* Condition 2: The values are all dictionaries.
* Condition 3: There is no case where the input is empty.


>>>P7({
    'jgoodall' : {'surname' : 'Goodall',
                'forename' : 'Jane',
                'born' : 1934,
                'died' : None,
                'notes' : 'primate researcher',
                'author' : ['In the Shadow of Man','The Chimpanzees of Gombe']},
    'rfranklin' : {'surname' : 'Franklin',
                'forename' : 'Rosalind',
                'born' : 1920,
                'died' : 1957,
                'notes' : 'contributed to discovery of DNA'},
    'rcarson' : {'surname' : 'Carson',
                'forename' : 'Rachel',
                'born' : 1907,
                'died' : 1964,
                'notes' : 'raised awareness of effects of DDT',
                'author' : ['Silent Spring']}
    })
False
Explanation: The value of 'rfranklin' doesn't contain the 'author' key.)

>>>P7({'a':{'aa':123, 'ab':[1,2]}, 'b':{'aa':'bb', 'ab':'cc'}})
True
Explanation: All values have exactly the same keys. {'aa', 'ab'}

"""


def P7(dct):
    
    #return type: boolean
    return
    
    