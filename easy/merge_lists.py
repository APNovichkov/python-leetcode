# For HOMEWORK 4

def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                # Dont do anything, just increase nums1 pointer
                i += 1
            else:
                # Have to insert nums2[j] at the nums1[i] index, but shift everything to the right
                nums1[i + 1:m + 1] = nums1[i:m]
                nums1[i] = nums2[j]
                j += 1
                i += 1
                m += 1

        if i == m:
            nums1[m:] = l2[j:]


if __name__ == '__main__':
    l1 = [1, 2, 7, 8, 0, 0]
    m = 4
    l2 = [2, 5, 6]
    n = 3
    merge(l1, m, l2, n)
    print('Out: {}'.format(l1))
