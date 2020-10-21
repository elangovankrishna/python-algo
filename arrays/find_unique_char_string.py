# Give a string return boolean value to determine if that has unique char or not.


def uni_char(s):

    if len(s) == 1:
        return True

    seen = set()

    for letter in s:

        if letter in seen:
            return False
        else:
            seen.add(letter)
    return True


s = 'abcde'
print(uni_char(s))