"""
Programmers sometimes use a dictionary of dictionaries as a simple database.
For example, to keep track of information about famous scientists, you might
have a dictionary where the keys are strings and the values are dictionaries,
like this:
{
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
}
Implement a function that returns the set of keys used in any of the inner dictionaries. 

* Condition 1: There is no case where the value of value is dictionary or the value of value of value is dictionary ... so on)
* Condition 2: The values are all dictionaries.
* Condition 3: There is no case where the input is empty.


>>>P6({
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
{'author', 'born', 'died', 'forename', 'notes', 'surname'}
"""

def P6(dct):

    return