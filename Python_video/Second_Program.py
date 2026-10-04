list1 = [1, 2, 4, 5]
n = max(list1)
expected_sum = n * (n + 1) // 2
actual_sum = sum(list1)
missing_num = expected_sum - actual_sum
print("Expected missing number is", missing_num)
