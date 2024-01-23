from algorithms.find_median_sorted_arrays import Solution



def test_find_median_sorted_arrays_success():
    obj = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    assert obj.findMedianSortedArrays(nums1, nums2) == 2.0
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert obj.findMedianSortedArrays(nums1, nums2) == 2.5


