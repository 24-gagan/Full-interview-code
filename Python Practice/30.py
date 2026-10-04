import math
def area(shape,*args,**kwargs):
    if shape=="circle":
        return math.pi*args[0]**2
    elif shape=="rectangle":
        return kwargs["length"]*kwargs["width"]
    else:
        return "Unknown shape"
print(area("circle",5))
print(area("rectangle",length=4,width=5))