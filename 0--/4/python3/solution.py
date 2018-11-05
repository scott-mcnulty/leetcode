class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        combined_lists = sorted(nums1 + nums2)
        
        # We have an even length list of combined values
        if len(combined_lists) % 2 == 0:
            lower_middle = len(combined_lists) // 2 - 1
            return (combined_lists[lower_middle] + combined_lists[lower_middle + 1]) / 2
        # Odd length
        else:
            return combined_lists[len(combined_lists) // 2]