class Student:
    def __init__(self, math, eng, bng):
        self.math = math
        self.english = eng
        self.banga = bng

    def get_avarage(self):
        return str((self.math + self.english + self.banga) / 3) + '%'

    @property
    def avarage_marks(self):
        return str((self.math + self.english + self.banga) / 3) + '%'

stu1 = Student(89, 90, 99)

print(stu1.get_avarage())
print(stu1.avarage_marks)
stu1.banga = 95
print(stu1.avarage_marks)
