def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    output = set()
    for num in nums:

        print(f"printing num {num}")
        pair = target - num
        if pair in output:

            return [num, pair]
        else:
            output.add(num)
            print(f" printing out {output}")


print(twoSum([3,2,4], 6))