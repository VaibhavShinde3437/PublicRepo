
# Here we using the open function and passing argument like name of the file and mode. we are using write mode which creates a new file everytime we open a file and erase old data and write new data in it

# name = input("What's your name")
# file = open("names.txt", "w")
# file.write(name)
# file.close

# ====================================================================================================================================================

# Here we are using append mode which will add data to the without erasing the old data

# name = input("What's our name? ")
# file = open ("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# ====================================================================================================================================================

# Here we are using with keyword to automate the closing process of file

# name = input("What's your name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# ====================================================================================================================================================

# Reading from a file

# with open("names.txt", "r") as file:
#     lines = file.readlines() # storing each line in a list
#     # lines = file.readline() # storing each word from a line
# for line in lines:
#     print(line.rstrip())


# names = []
# with open("names.txt") as file: # read mode is defualt if mode is not mentioned
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names):
#     print(name)

# =========================================================================================================================================================
# reading writing in csv file

# with open("student.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is from {row[1]}")
#         name, address = line.rstrip().split(",")
#         print(f"{name} : {address}")


# with open("student.csv") as file:
#     for line in file:
#         name, address = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["address"] = address
#         print(f"{student['name']} is from {student['address']}")  


# Using "csv" module to work with csv files
import csv
# students = []
# with open("student.csv") as file:
#     reader = csv.reader(file)
#     for name, address in reader:
#         students.append({'name': name, 'address' : address})
# for student in sorted(students, key=lambda student : student['name']):
#     print(f"{student['name']} is from {student['address']}")
    
# Writing in a csv file
name = input("What's your name? ")
address = input("What's your address? ")
with open("student.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,address])
