# The problem:
#  - Return the index of the first occurance of the needle in the haystack.
#    Return -1 if needle is not found in the haystack

# Clarifications:
# - So input is two strings, where one is haystack and one is needle?
# - Can needle be larger than the haystack, or is good input guaranteed?
# - Output should be just a number?
# - What to return if either of the strings are empty

# Assumptions:
# - Input is indeed just two strings and good input is guaranteed
# - Output should just be one number
# - Return 0 when needle or haystack is an empty string

# Sample input 1:
# Haystack - "hello"
# Needle - "ll"
# Output - "2"

# Sample input 2:
# Haystack - "aaaaa"
# Needle - "baa"
# Output - "-1"

# Initial thoughts:
# - Need to run through the whole haystack forsure. Then check for the first character of the needle to the current
#   character of the haystack, if they match, remember the index that we were at in in the haystack and move 1 char over in both
#   the haystack and needle list. Keep going until we either all chars match, in which case we should break and return that saved index,
#   or if we have a non-match, we need to return to the index+1 of where we left off and continue the search in similar fashion.

# Additional thoughts:
# - There might be a way to do this with a stack... But let's try the above method. It works!

def strStr(haystack, needle):

    haystack_len = len(haystack)
    needle_len = len(needle)

    # Edge case
    if needle == "":
        return 0

    # Run through haystack
    for i in range(haystack_len):
        # Break if at this point needle is too big to fit in the remaining haystack
        if i > haystack_len - needle_len:
            break

        # Run through needle for every char in haystack
        for j in range(needle_len):
            # If needle char matches haystack char go into if
            if haystack[i + j] == needle[j]:
                # If at the end of needle, we have a match, and return match index, which is i
                if j == needle_len - 1:
                    return i
            else:
                # If at any moment we dont have a match, break from needle loop and continue
                break

    return -1  # Return -1 if no match


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"

    print(f"Haystack: {haystack}")
    print(f"Needle: {needle}")

    print(f"First occurance of needle: {strStr(haystack, needle)}")
