import heapq


def find_kth_largest(nums, k):
    # Use a min-heap to keep the largest k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    # Iterate through the rest of the array
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    # The root of the heap is the kth largest element
    return min_heap[0]


# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 3
print(f"The {k}th largest element is {find_kth_largest(nums, k)}")

