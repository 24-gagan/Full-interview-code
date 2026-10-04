class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_salary(self):
        return self.salary
    def set_salary(self,salary):
        if salary>0:
            self.salary=salary
        else:
            print("invalid salary")
s1=Employee("gagan",1000)
print(s1.get_salary())
print(s1.set_salary())
s1.set_name("Amit")
s1.set_salary(60000)

print(s1.get_name())
print(s1.get_salary())