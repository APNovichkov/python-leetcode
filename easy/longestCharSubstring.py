def find_longest_substring(input):
    max_length = 0
    char_set = set()
    max_substring = [0, 0]
    i = 0
    j = 0

    while j < len(input):
        if input[j] in char_set:
            if len(char_set) > max_length:
                max_length = len(char_set)
                max_substring = [i, j]
                j = i + 1
                i += 1
            else:
                j = i + 1
                i += 1

            char_set = set()
        else:
            char_set.add(input[j])
            j += 1

        if len(char_set) > max_length:
            max_substring = [i, j]

    return input[max_substring[0]:max_substring[1]]


if __name__ == '__main__':
    input = 'mistsissippi'
    print(f'Longest substring in {input} is {find_longest_substring(input)}')
