def rotate_in_place(nums, k):
    n = len(nums)
    k = k % n  # In case k is greater than the length of the array

    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n-1)  # Step 1: Reverse the entire array
    reverse(0, k-1)  # Step 2: Reverse the first k elements
    reverse(k, n-1)  # Step 3: Reverse the remaining n-k elements

# Example usage:
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate_in_place(nums1, k1)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
k2 = 2
rotate_in_place(nums2, k2)
print(nums2)  # Output: [3, 99, -1, -100]
