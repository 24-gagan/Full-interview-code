original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict={k:v for (k,v) in original_dict.items() if v%2==0}
print(even_dict)