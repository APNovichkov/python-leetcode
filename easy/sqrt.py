# Problem:
# - Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# - Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Clarifications:
# - So if we input 4 we should get 2, and if we input 8, we should also get 2, right?
# - If x is 0 we should return 0?

# Assumptions:
# - Yes to the first part
# - If we get 0, we should return 0

# Sample input:
# - 8 -> 2
# - 4 -> 2
# - 2 -> 1
# - 9 -> 3

# Initial thoughts:
# - Well, easiest way is to run through integers up to 8, and square them and see if the output is
#   equal to x, and keep track of the previous integer. If at any point we get squared product that is
#   larger than x, we need to return that previous integer. Ok this one fails memory in leetCode.. but it is a working solution!

# More thoughts
# - Need to use a while loop instead of a for loop, that way we save memory.
# - This ends up being slow anyways, and only beats 5% of accepted submissions on leetcode, but it submitted and passed!

# Additional thoughs:
# - Need to figure out where to start the loop. Kinda see if we can figure out the largest number that we can get
#   without going over the actual answer... Am not sure how to do that though....

def mySqrt(x):
    if x == 0:
        return 0

    i = 0
    while True:
        if i**2 <= x:
            prev = i
        else:
            return prev
        i += 1

    return prev


if __name__ == "__main__":
    x = 4
    print(f"Square root of {x} is {mySqrt(x)}")
