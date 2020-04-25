# Variable Table

# Input - abcabcd
# Output - abcd

# c_letter - a,b,c,a,b
# i -> 0,0,0,1
# j -> 0,1,2,1
# char_set -> (a, b, c), () ....
# max_length -> 3

def lengthOfLongestSubstring(self, s):
    """Working solution to problem, pretty slow though could be faster"""

    if len(s) == 1:
        return 1

    max_length = 0
    char_set = set()
    i = 0
    j = 0

    while j < len(s):
        if s[j] in char_set:
            if len(char_set) > max_length:
                max_length = len(char_set)
                j = i + 1
                i += 1
            else:
                j = i + 1
                i += 1

            char_set = set()
        else:
            char_set.add(s[j])
            j += 1

    max_length = max(len(char_set), max_length)

    return max_length
