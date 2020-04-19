def addBinary(a, b):
    out = ''

    i = len(a) - 1
    j = len(b) - 1

    rem = 0
    res = 0

    while i >= 0 or j >= 0:
        if i < 0:
            a_i = 0
        else:
            a_i = int(a[i])

        if j < 0:
            a_j = 0
        else:
            a_j = int(b[j])

        res = (rem + a_i + a_j) % 2
        rem = (rem + a_i + a_j) // 2

        out = f'{res}{out}'

        i -= 1
        j -= 1

    if rem == 1:
        out = f'{rem}{out}'

    return out


if __name__ == '__main__':
    # Different test cases:

    # ** Could try empty string but in the problem spec it said it would not be empty

    # Edge Case - Output should be 0
    i1_1 = '0'
    i1_2 = '0'
    print(f"Sum of {i1_1} and {i1_2} is {addBinary(i1_1, i1_2)}")

    # Test Case 1 - Output should be 10
    i2_1 = '1'
    i2_2 = '1'
    print(f"Sum of {i2_1} and {i2_2} is {addBinary(i2_1, i2_2)}")

    # Test Case 2 - Output should be 10101
    i3_1 = '1010'
    i3_2 = '1-11'
    print(f"Sum of {i3_1} and {i3_2} is {addBinary(i3_1, i3_2)}")
