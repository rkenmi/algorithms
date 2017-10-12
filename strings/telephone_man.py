
def telephone(s):
    """

    :param s: a string of digits representing a 7 or 10 digit phone number. assumes no `-` sign
    :return: a list of permutations of strings with alphanumerical representations (for digits 2-9)
    """
    keypad = {
       '2': 'abc',
       '3': 'def',
       '4': 'ghi',
       '5': 'jkl',
       '6': 'mno',
       '7': 'pqrs',
       '8': 'tuv',
       '9': 'wxyz',
    }

    def recurse(s):
        if s == '':
            return ['']

        new = []

        alpha = keypad.get(s[0], s[0])
        for c in alpha:
            known = recurse(s[1:])
            for x in known:
                new.append(c + x)

        return new

    return recurse(s)

