from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # cnt1= Counter(nums1)
        # cnt2= Counter(nums2)
        # ans = []
        # set1 = set(nums1)
        # set2 = set(nums2)
        # for i in set1 or set2:
        #     for rep in range(min(cnt1[i], cnt2[i])):
        #         ans.append(i)
        # return ans

        # more efficient:
        ans = []
        if len(nums2)> len(nums1):
            nums1, nums2 = nums2, nums1
        cnt1 = Counter(nums1)
        for i in nums2:
            if i in cnt1 and cnt1[i]>0:
                ans.append(i)
                cnt1[i] = cnt1[i] - 1
        return ans

