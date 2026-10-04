arr=[1,2,3,4,5]
def left(arr):
    return arr[2:]+arr[:2]
print(left(arr))