str1 = "Hi this is Gagandeep.Gagandeep is giving interview for Zebra, Have a nice day Gagandeep"


def count_each_alphabet(s):
    s = s.lower()  # ignore case
    freq = {}

    for ch in s:
        if ch.isalpha():
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

    for k, v in freq.items():
        print(k, ":", v)


count_each_alphabet(str1)
"""  Firstly string is converted to lower case and then we check the alphabet and count the frequency"""
