def manhattan(p1, p2):

    '''
    Calculate the Manhattan distance between two points.
    '''

    d_man = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    return d_man