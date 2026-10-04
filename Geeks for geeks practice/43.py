def largest(arr):
    max=arr[0]
    for i in arr:
        if i>max:
            max=arr[i]
    return max
arr=[1,2,3,4,5]
print(largest(arr))