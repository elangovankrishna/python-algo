'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
'''


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    """
    nums.sort()
    print(nums)
    res = set()
    lookupDict = {}

    for i in range(len(nums)):
        lookupDict[nums[i]] = i

    # {-4: 0, -1: 2, 0: 3, 1: 4, 2: 5}

    for i in range(len(nums)):
        if i != 0 and nums[i] == nums[i - 1]: # since its sorted
            continue
        twoSum = -nums[i]
        print(f"printing two sum -- {twoSum}")
        for j in range(i + 1, len(nums)):
            target = twoSum - nums[j]
            print(f"printing target -- {target}")
            if target in lookupDict and lookupDict[target] > j:
                print(f"Adding element to result")
                res.add((-twoSum, nums[j], target))
    return res



print(threeSum([-1,0,1,2,-1,-4]))