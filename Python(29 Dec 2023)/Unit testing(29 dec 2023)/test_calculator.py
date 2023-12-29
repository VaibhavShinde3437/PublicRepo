
from calculator import addition
from calculator import subtract
from calculator import multiplication
from calculator import divide




# using conditionals like "if-else" to test the code 
# def main():
#     sucess = 0;
#     failed = 0
#     if(addition(2,3) != 5):
#         print("Additon is not 5")
#         failed = failed + 1
#     else : sucess = sucess + 1
#     if(addition(112,69) != 181):
#         print("Additon is not 181")
#         failed = failed + 1  
#     else : sucess = sucess + 1
#     if(subtract(2,1) != 1):
#         print("Subtraction is not 1")
#         failed = failed + 1
#     else : sucess = sucess + 1
#     if(subtract(83,57) != 26):
#         print("Subtraction is not 5")
#         failed = failed + 1
#     else : sucess = sucess + 1 
#     if(multiplication(2,2) != 4):
#         print("Multiplication is not 4")
#         failed = failed + 1
#     else : sucess = sucess + 1
#     if(multiplication(87,15) != 1305):
#         print("Multiplication is not 1305")
#         failed = failed + 1
#     else : sucess = sucess + 1
#     if(divide(4,2) != 2):
#         print("Division is not 2")
#         failed = failed + 1
#     else : sucess = sucess + 1
#     if(divide(63,5) != 12.6):
#         print("Division is not 12.6")
#         failed = failed + 1
#     else : sucess = sucess + 1

#     print("Testcases Passed :", sucess)
#     print("Testcases failed :", failed)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# Testing code using assert keyword but needs to handle the assertion error for every testcase
# def main():
    
#     try:
#         assert addition(2,3) == 5
#     except AssertionError:
#         print("Additon is not 5")
#     try:
#         assert addition(112,69) == 181
#     except AssertionError:
#         print("Additon is not 181")
#     try:
#         assert subtract(2,1) == 1
#     except AssertionError:
#         print("Subtraction is not 1")
#     try:
#         assert subtract(83,57) == 26
#     except AssertionError:
#         print("Subtraction is not 26")
#     try:
#         assert multiplication(2,2) == 4
#     except AssertionError:
#         print("Multiplication is not 4")
#     try:
#         assert multiplication(87,15) == 1305
#     except AssertionError:
#         print("Multiplication is not 1305")
#     try:
#         assert divide(4,2) == 2
#     except AssertionError:
#         print("Division is not 2")
#     try:
#         assert divide(63,5) == 12.6
#     except AssertionError:
#         print("Division is not 12.6")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# using "pytest" for unti testing
import pytest

def add():
    assert addition(2,3) == 5
    # assert addition(112,69) == 181, "Addition is not 181"
    # assert subtract(2,1) == 1, "Subtraction is not 1"
    # assert subtract(83,57) == 26, "Subtraction is not 26"
    # assert multiplication(2,2) == 4, "Multiplication is not 4"
    # assert multiplication(87,15) == 1305, " Multiplication is not 1305"
    # assert divide(4,2) == 2, "Division is not 2"
    # assert divide(63,5) == 12.6, "Division is not 12.6"

    


# if __name__ == "__main__":
#     main()