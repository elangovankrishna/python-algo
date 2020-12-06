def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    check = []
    ix = 0
    mapping = {'}': '{', ']': '[', ')': '('}
    while ix < len(s):

        print(f"printing index -- {ix}")

        print(f"printing s at index -- {s[ix]}")

        if s[ix] in mapping.values():
            check.append(s[ix])

        else:
            print(f"printing check -1 -- {check[-1]}")
            print(f"printing check -- {check}")
            if check and mapping[s[ix]] == check[-1]:

                print(f"poping element -- {check}")
                check.pop()
            else:
                print(f"adding element -- {check}")
                check.append(s[ix])

                if check[0] in mapping.keys():
                    return False

        ix += 1

    return not check


print(isValid("([]{)"))

"()([]{})"

"""
"([)]"

"([])"

"()([]{})"

0 1 2 3 

"""


def isValid1(s: str) -> bool:
    dic = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    stack = []

    for i in list(s):
        if i in dic.keys():
            stack.append(i)
        else:
            if len(stack) > 0 and i == dic[stack.pop()]:
                next
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print(isValid1("([]{)"))