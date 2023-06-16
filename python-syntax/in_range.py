def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """
    if lowest >= nums[0] and lowest <= nums[len(nums) - 1]:
        print(f"{lowest} fits")
    if highest >= nums[0] and highest <= nums[len(nums) - 1]:
        print(f"{highest} fits")
    # YOUR CODE HERE


in_range([10, 20, 30, 40, 50], 15, 30)            
