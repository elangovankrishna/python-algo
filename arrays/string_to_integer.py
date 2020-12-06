
def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """

    non_wht_s = s.strip()
    sign = ('+', '-')
    out = ''

    if len(non_wht_s) < 1 or len(non_wht_s) > 200 or (len(non_wht_s) == 1 and not non_wht_s[0].isnumeric()):
        return 0

    if len(non_wht_s) > 1 and not non_wht_s[0].isnumeric() and not non_wht_s[0] in sign:
        return 0


    for ele in range(len(non_wht_s)):

        if len(out) > 1 and non_wht_s[ele-1] in sign:
            return 0

        if non_wht_s[ele].isnumeric() or non_wht_s[ele] in sign:
            out += non_wht_s[ele]
        elif ele > 0:
            break

    print(out)
    try:
        if len(out) > 1 and out[0] in sign:
            if int(out[1:]):
                print("inside if")
                if int(out) > (2 ** 31) - 1:
                    return (2 ** 31) - 1
                elif int(out) < (-2 ** 31):
                    return (-2 ** 31)
                else:
                    return int(out)
        else:

            if int(out) > (2 ** 31) - 1:
                return (2 ** 31) - 1
            elif int(out) < (-2 ** 31):
                return (-2 ** 31)
            else:
                return int(out)
    except:
        return 0



print(myAtoi("   +0a"))
