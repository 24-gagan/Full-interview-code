def comress_string(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)


s = "aabcccccaaa"
print(comress_string(s))
