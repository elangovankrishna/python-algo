# Array pair sum, given a array list find the pair that adds upto the target.

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

def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    output = {}
    for i in range(len(nums)):

        print(f"printing num {nums}")
        k = target - nums[i]
        if k in output:

            return [output[k], i]
        else:
            output[nums[i]] = i
            print(f" printing out {output}")


print(twoSum2([3,2,4], 6))