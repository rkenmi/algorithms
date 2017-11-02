
def encircular(commands):
    counter = 0
    pos = origin = [0, 0]
    move = [0, 1]  # default move vector

    while counter < 4:
        for cmd in commands:
            if cmd == 'G':  # move forward (by vector)
                pos = [pos[0] + move[0], pos[1] + move[1]]
            elif cmd == 'L':  # turn left
                move = [-move[1], move[0]]
            elif cmd == 'R':  # turn left
                move = [move[1], -move[0]]
        if pos[0] == origin[0] and pos[1] == origin[1]:
            return True  # is circular

        counter += 1

    return False
