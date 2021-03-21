"""
There is a set of words and a query word.
You must change exactly one character of the query word.
Implement a function that determins whether the changed word can be the element of the set.

* Condition: Words consist of only lower-case alphabet(s) and no space.


>>>P10({"data", "science"}, "data")
False
Explanation: If you change one character of the query word, there is no matching word in the set.

>>>P10({"data", "science"}, "daaa")
True
Explanation: You can change one alphabet to make "daaa" -> "data" .

>>>P10({"data", "science"}, "scienzz")
False

>>>P10({"data", "science", "scienze"}, "scienzz")
True

>>>P10({"data", "science"}, "dataa")
False
"""


def P10(word_set, query_word):
    """
    Key strategy
    1. Compare the word length
    2. If the length is same, iterate over each character.
    3. if len(set[index])-match_count == 1 -> return true
    """

    result = False
    match_count = 0

    for word in word_set:
        # 1. compare word length
        if len(word) == len(query_word):
            # 2. if length equals, compare each char
            for j, char in enumerate(word):
                if char == query_word[j]:
                    match_count += 1
            # 3. if condition match, update result and break the loop
            if len(word) - match_count == 1:
                result = True
                break
        # for next word, initialize match_count
        match_count = 0

    return result