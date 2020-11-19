def findNumber(arr, k):
    # Write your code here

    print(arr)

    arr.sort()

    print(arr)

    if len(arr) < 1:
        return 'No'

    if k in arr:
        return 'Yes'

print(findNumber([2,1,3,5], 1))