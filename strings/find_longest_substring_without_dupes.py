def find_longest_substring_without_dupes(s):
    if len(s) == 0:
        return ""

    s_l = list(s)

    seen = set(s[0])
    slow, fast = 0, 1
    result = []

    while slow < fast and fast < len(s_l):
        if s_l[fast] in seen:
            result = s_l[slow:fast] if fast - slow > len(result) else result
            seen.remove(s_l[slow])
            slow += 1
        else:
            seen.add(s_l[fast])
            fast += 1

    result = s_l[slow:fast] if fast - slow > len(result) else result
    return "".join(result)
