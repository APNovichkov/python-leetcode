# Input - 2,5,7,11,15 target = 9
# Output - [1,3]

# i - 0
# j - 4, 3, 2
# nums[i] - 2
# nums[j] - 15, 11, 7
# n_sum - 17, 13, 9** GOT A MATCH

def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    # 2,5,7,11,15 target = 9
    # 1 2 3 4  5

    i = 0
    j = len(numbers) - 1

    while i <= j:
        n_sum = numbers[i] + numbers[j]
        if n_sum == target:
            return [i + 1, j + 1]

        if n_sum > target:
            j -= 1
        else:
            i += 1
