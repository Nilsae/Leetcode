class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Initialize pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # Pointer for the end of merged array
        p = m + n - 1
        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are elements left in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        return nums1
print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))