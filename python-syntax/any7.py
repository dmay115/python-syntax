def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    count = nums.count(7)
    return False if (count == 0) else True
    # YOUR CODE HERE 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

