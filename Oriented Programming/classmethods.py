#Class methods = Allow operations related to the class itself
#                Take (cls meaning Class) as the first parameter, which represents the class itself

class Student:

    # class variables
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        # instances variables
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The average gpa is : {cls.total_gpa/cls.count:.2f}"

student1 = Student("Henri", 18)
student2 = Student("George", 8)
student3 = Student("Cindy", 20)
student4 = Student("Laura", 16)

print(Student.get_count())
print(Student.get_average())

# Uniquement des intéractions avec les variables de classe pour les classmethod