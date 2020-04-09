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

        sample_counter = 0

        while i < m and j < n:

            if nums1[i] < nums2[j]:
                # Dont do anything, just increase nums1 pointer
                i += 1
            else:
                # Have to insert nums2[j] at the nums1[i] index, but shift everything to the right
                print(f'Nums1: {nums1}')
                nums1[i + 1:m + 1] = nums1[i:m]
                print(f'Nums1: {nums1}')
                nums1[i] = nums2[j]
                j += 1
                i += 1
                m += 1

            sample_counter += 1
            if sample_counter > 10:
                break

        

        print(f'Nums1: {nums1}')
        pass


if __name__ == '__main__':
    l1 = [1, 2, 3, 0, 0, 0]
    m = 3
    l2 = [2, 5, 6]
    n = 3
    merge(l1, m, l2, n)
    print('Out: {}'.format(l1))
