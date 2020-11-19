# Create a function that takes a integer and computes the cumulative sum of 0 to that integer

def rec_sum(n):

    if n == 1:
        return n
    else:
        return n + rec_sum(n-1)


print(rec_sum(5))


def sumOfNnum(n):

    if n == 1:
        return n
    else:
        return n+ (n * (n-1))/2


print(sumOfNnum(5))