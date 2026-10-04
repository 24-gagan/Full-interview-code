def func(*args):
    return sum(args)
print(func(1,2,3))

def func(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
func(a=1,b=2,c=3)