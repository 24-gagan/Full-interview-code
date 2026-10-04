#s1 = "Yn"
#s2 = "PYnative"

def balanced(s1,s2):
    for char in s1:
        if char not in s2:
            return False
        return True
s1 = "Yn"
s2 = "PYnative"
print("balanced" if balanced(s1,s2) else "Not balanced")
