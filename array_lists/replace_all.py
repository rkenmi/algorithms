# assumes that A has enough space to contain the words
def replace_all(A, word):
    # count blanks
    blanks = 0
    size = 0
    for i, c in enumerate(A):
        if c == ' ':
            blanks += 1
        elif c is None:
            break
        size += 1

    # the word 'blank' is 5 characters, but we want to replace the 'space', so allocate 4 characters per 'space'
    last_char_ptr = size
    final_char_ptr = final_size = size + ((len(word) - 1) * blanks)

    while last_char_ptr > 0:
        if A[last_char_ptr] != ' ':
            A[final_char_ptr] = A[last_char_ptr]
            final_char_ptr -= 1
        else:
            ctr = len(word) - 1
            while ctr >= 0:
                A[final_char_ptr] = word[ctr]
                ctr -= 1
                final_char_ptr -= 1

        last_char_ptr -= 1

    return "".join(A[:final_size])




