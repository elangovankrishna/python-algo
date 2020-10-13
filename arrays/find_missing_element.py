# Find the missing element from two given array

lst1 = [5,5,6,7,8]
lst2 = [5,6,7,8]

# Solution 1 this is big O of (O N(log n))

import collections
def finder1(lst1, lst2):

    dict = collections.defaultdict(int)

    for ele in lst2:
        dict[ele] += 1

    for ele in lst1:

        if dict[ele] == 0:
            return ele
        else:
            dict[ele] -= 1


print(finder1(lst1, lst2))