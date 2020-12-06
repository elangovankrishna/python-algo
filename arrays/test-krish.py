
def twosum(nums, k):

    # [3, 1, 5, 6], 4
    # [1,3,5,6]
    # [4], 4
    # True or False

    if not len(nums) > 2:

        return False

    for i in range(len(nums)):  # O(N)

        for j in range(i+1, len(nums)):

            if nums[i] + nums[j] == k:

                return True
            else:

                return False

# Time complexity O(N2)


def twosum2(nums, k):


    if not len(nums) > 2:
        return False


    nums.sort()
    # [1,4,5,6], 4

    for i in range(1, len(nums)):

        if nums[i] >= k or nums[i-1] >=k:

            return False
        else:

            if nums[i-1] + nums[i] == k:

                return True
            else:

                return False

# Time Complexity of O(N)




