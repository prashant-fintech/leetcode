def rotate(nums, k):
    n = len(nums)
    k = k % n  # In case k is greater than the length of the array
    nums[:] = nums[-k:] + nums[:-k]

# Example usage:
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate(nums1, k1)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
k2 = 2
rotate(nums2, k2)
print(nums2)  # Output: [3, 99, -1, -100]