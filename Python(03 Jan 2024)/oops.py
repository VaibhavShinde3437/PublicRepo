#Inheritance

# class College:
#     def __init__(self, name, cName):
#         if not name:
#             raise ValueError("Missing name attribute")
#         self.name = name
#         if not cName:
#             raise ValueError("Missing cName attribute")
#         self.cName = cName        

# class Student(College):
#     def __init__(self, name, cName, stream):
#         super().__init__(name, cName)
#         self.stream = stream

#     def __str__(self):
#         return f"Name : {self.name}, College : {self.cName}, Stream : {self.stream}" 

# class Teacher(College):
#     def __init__(self, name, cName, subject):
#         super().__init__(name, cName)
#         self.subject = subject

# def main():
#     name = input("Name? ")
#     cName = input("College name? ")
#     stream = input("Stream? ")

#     student = Student(name, cName, stream)
#     print(student)

# if __name__ == "__main__":
#     main()

# ========================================================================================================================================================

#opeartor overloading

# class Student:
#     def __init__(self, maths, bio, phy):
#         self.maths = maths
#         self.bio = bio
#         self.phy = phy
    
#     def __str__(self):
#         return f"Maths : {self.maths}, Biology : {self.bio}, Physics : {self.phy}"

#     def __add__(self, other):
#         maths = self.maths + other.maths
#         bio = self.bio + other.bio
#         phy = self.phy + other.phy
#         return Student(maths,bio,phy)
    
#     def __sub__(self, other):
#         maths = self.maths - other.maths
#         bio = self.bio - other.bio
#         phy = self.phy - other.phy
#         return Student(maths,bio,phy)
    
#     def __ge__(self, other):
#         student1 = self.maths+self.bio+self.phy
#         student2 = other.maths+other.bio+other.phy

#         if student1>student2:
#             return "student1 have more marks than student2"
#         if student1==student2:
#             return "student1 and student2 have same marks"

# def main():
#     student1 = Student(67, 55, 92)
#     student2 = Student(67, 55, 92)

#     total = student1 >= student2
#     print(total)

# main()



