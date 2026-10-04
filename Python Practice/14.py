def val(num):
    for i in num:
        yield i
gen=val([1,2,3,4,5])
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))