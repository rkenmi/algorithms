def replace_all(s):
    # count blanks
    blanks = 0
    for c in s:
        if c == ' ':
            blanks += 1

    # the word 'blank' is 5 characters, but we want to replace the 'space', so allocate 4 characters per 'space'
    s_array = list(s) + ([0] * (blanks * 4))

    last_char_ptr = len(s) - 1
    final_char_ptr = len(s_array) - 1

    blank_str = 'blank'
    while last_char_ptr > 0:
        if s[last_char_ptr] != ' ':
            s_array[final_char_ptr] = s[last_char_ptr]
            final_char_ptr -= 1
        else:
            ctr = 4
            while ctr >= 0:
                s_array[final_char_ptr] = blank_str[ctr]
                ctr -= 1
                final_char_ptr -= 1

        last_char_ptr -= 1

    return "".join(s_array)




