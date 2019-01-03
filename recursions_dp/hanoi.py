def hanoi(num_rings):

    def _hanoi(num_of_rings_to_move, from_peg, to_peg, intermediary_peg):
        if num_of_rings_to_move > 0:
            steps = _hanoi(num_of_rings_to_move - 1, from_peg, intermediary_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            steps += 1
            steps += _hanoi(num_of_rings_to_move - 1, intermediary_peg, to_peg, from_peg)

            return steps
        return 0


    pegs = [[0] * num_rings, [], []]

    return _hanoi(num_rings, 0, 1, 2)

