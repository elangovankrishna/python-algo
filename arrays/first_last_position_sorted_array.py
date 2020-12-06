
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
"""

def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    if len(nums) == 0:
        res = [-1, -1]
        return res

    res = []
    indx = 0
    for ele in range(len(nums)):

        if target == nums[ele]:
            if len(res) > 1:
                res.pop()
                res.append(ele)
            else:
                indx = ele
                res.append(ele)

    if len(res) == 0:
        res = [-1, -1]

    if len(res) == 1:
        res.append(indx)

    return res