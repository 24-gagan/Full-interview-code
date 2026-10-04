class Student:
    school_name="Army School Pathankot"
    def __init__(self,name):
        self.name=name


    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @staticmethod
    def is_passing_marks(marks):
        return marks>40

s1=Student("Gagan")
print(Student.get_school_name())

print(Student.is_passing_marks(55))
print(Student.is_passing_marks(35))