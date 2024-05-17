def two_sum(numbers, target):
    """
    Takes a list of numbers and a target sum and returns the indices of the two numbers that sum to target. .
    :param numbers:
    :param target:
    :return: list of indices of the two numbers that sum to target
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-indexed positions
        elif current_sum < target:
            left += 1
        else:
            right -= 1


# Example usage
numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))  # Output: [1, 2]

numbers = [1, 2, 3, 4, 4, 9, 11, 15]
target = 8
print(two_sum(numbers, target))  # Output: [4, 5]
