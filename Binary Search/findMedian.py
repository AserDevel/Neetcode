class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sorted_nums = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sorted_nums.append(nums1[i])
                i += 1
            else:
                sorted_nums.append(nums2[j])
                j += 1
        
        if i < len(nums1):
            sorted_nums.extend(nums1[i:])
        elif j < len(nums2):
            sorted_nums.extend(nums2[j:])
        
        mid = len(sorted_nums) // 2
        
        if len(sorted_nums) % 2 == 0:
            median = (sorted_nums[mid] + sorted_nums[mid - 1]) / 2
        else:
            median = sorted_nums[mid]
        
        return median

