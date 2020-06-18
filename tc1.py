"""
ABCDE
FGHIJ
KLMNO
PQRST
UVWXY
Z0123
"""

char_matrix = [list('ABCDE'), list('FGHIJ'), list('KLMNO'), list('PQRST'), list('UVWXY'), list('Z0123')]
start_position = (3, 2)

question = input().strip().split(', ')

def process_query(query):
    global start_position, char_matrix

    if query == '(space)':
        return ' '

    start = [*start_position]
    for i in range(0, len(query), 2):
        direction = query[i: i+2]
        if direction[0] == 'R':
            start[1] += int(direction[1])
            start[1] %= 5
        elif direction[0] == 'L':
            start[1] -= int(direction[1])
            start[1] %= 5
        elif direction[0] == 'U':
            start[0] -= int(direction[1])
            start[0] %= 6
        elif direction[0] == 'D':
            start[0] += int(direction[1])
            start[0] %= 6
    return char_matrix[start[0]][start[1]]

print(''.join([process_query(query) for query in question]))


#L2U2R1D4R1U2