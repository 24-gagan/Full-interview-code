def insert_middle(original,new):
    mid=len(original)//2
    return original[:mid]+new+original[mid:]
s="Helloworld"
new_str="python"
result=insert_middle(s,new_str)
print(result)