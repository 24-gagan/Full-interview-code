s = "python sharpens your coding logic"  # ek string create karo


words = s.split()  # string split karke list create karo
longest = words[0]  # longest ko inital value assign karo
for word in words:  # loop iterate karo
    if len(word) > len(longest):  # length compare karo
        longest = word  # longest assign karo

print(longest)  # longest print karo
