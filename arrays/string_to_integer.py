
def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """

    non_wht_s = s.strip()


    if len(non_wht_s) < 1 or len(non_wht_s) > 200:
        return 0

    sign = ('+', '-')
    out = ''

    for ele in range(len(non_wht_s)):

        if non_wht_s[0].isalpha():
            return 0

        if non_wht_s[ele] in sign:
            out += non_wht_s[ele]

        if non_wht_s[ele].isnumeric():
            out += non_wht_s[ele]



    if int(out) > (2 ** 31) - 1:
        return (2 ** 31) - 1
    elif int(out) < (-2 ** 31):
        return (-2 ** 31)
    else:
        return int(out)


print(myAtoi("-91283472332"))