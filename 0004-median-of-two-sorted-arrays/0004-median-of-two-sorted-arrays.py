class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        total = m + n
        half = (total + 1) // 2
        
        low, high = 0, m

        while low <= high:

            mid1 = (low + high) // 2
            mid2 = half - mid1

            left1 = float("-inf") if mid1 == 0 else nums1[mid1 - 1]
            right1 = float("inf") if mid1 == m else nums1[mid1]

            left2 = float("-inf") if mid2 == 0 else nums2[mid2 - 1]
            right2 = float("inf") if mid2 == n else nums2[mid2]

            if left1 <= right2 and left2 <= right1:

                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2

                return max(left1, left2)

            elif left1 > right2:
                high = mid1 - 1
            else:
                low = mid1 + 1