# find if two given strings are anagram of each other, assume there is no capital words and remove spaces if any on
# those words

def anagram(s1, s2):


    if len(s1) == 0 or len(s2) == 0:
        return print("Length of strings are empty")

    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    seen = {}

    for letter_s1 in s1:

        if letter_s1 in seen:
            seen[letter_s1] += 1
        else:
            seen[letter_s1] = 1

    for letter_s2 in s2:

        if letter_s2 in seen:
            seen[letter_s2] -= 1
        else:
            seen[letter_s2] = 1

    for k in seen:
        if seen[k] != 0:
            return False

    return True



print(anagram('dog', 'god1'))