"""
**Instruction**
Please see instruction document.

"""


def P1(path: str) -> str:
    ##### Write your Code Here #####
    #first, strip
    path = path.strip()

    # if ends with '/', delete
    if path[-1] == '/':
        path = path[:-1]

    # replace // -> /
    path = path.replace('//', '/')

    # now the path is regular shape, which means it's like '/a/b/c/d'

    # split by '/' and delete ''
    paths = path.split('/')
    for item in paths.copy():
        if item == '':
            paths.remove('')

    # base case -> return '/'
    char_set = set(paths)
    char_set_length = len(char_set)
    # 1 when all are '.'
    if (char_set_length == 1) and (list(char_set)[0] == '.'):
        return '/'
    # 2 when all are '..'
    if (char_set_length == 1) and (list(char_set)[0] == '..'):
        return '/'
    # 3 just combination of '.' and '..'
    if (char_set_length == 2) and ('..' in list(char_set)) and ('.' in list(char_set)):
        return '/'

    # do things with depth and depth_path dict
    depth = 0
    depth_path = {}
    for item in paths:
        # if item == '.' -> depth += 0
        if item == '.':
            depth += 0
        # if item == '..' -> depth -=1 / if depth < 0 , depth = 0
        elif item == '..':
            depth -= 1
            if depth < 0:
                depth = 0
        # else add to dict and depth += 1
        else:
            depth_path[depth+1] = item
            depth += 1
    
    # if depth == 0, return '/'
    if depth == 0:
        return '/'
    # else, concantenate
    else:
        path = ""
        for i in range (depth):
            path += '/' + depth_path[i+1]
            
    
    return path
    ##### End of your code #####

