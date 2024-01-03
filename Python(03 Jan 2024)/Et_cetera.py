# def function() -> None:
#     '''This is to demonstrate docStrings'''

# print(function.__doc__)
# help(function)

# ===========================================================================================================================================================

# unpacking

# def add(a,b,c,d  ):
#     return a+b+c+d

# num = [1,23,4,5]
# print(add(*num))

# dict = {"a":2, "b":23,"c":4,"d":5}
# print(add(**dict))

# ===========================================================================================================================================================

# def fun(*args, **kwargs):
#     print("Positional :", args, "Named :", kwargs)

# fun(100,37,34,2,31,1,a=1,b=2,c=3)

# def fun(*args):
#     ans = 0
#     for num in args:
#         ans += num
#     return ans

# print(fun(1,2,3,4))

# arr = [1,2,3,4,5,6,7]
# # dict = {"a":2, "b":23,"c":4,"d":5}
# print(*arr)

# ===========================================================================================================================================================

# def greeting(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)


# greeting("my", "name", "is", "vaibhav")

# ==========================================================================================================================================================

# def add(numbers):
#     return numbers*numbers

# def fun(*number):
#     adding = map(add, number)

#     print(*adding)

# fun(1,2,3,4)

# ==========================================================================================================================================================

# def add(numbers):
#     return numbers*numbers

# def fun(*number):
#     adding = [add(num) for num in number]

#     print(*adding)

# fun(1,2,3,4,5,6,7,8,9)

# ==========================================================================================================================================================

# dict = {"a":2, "b":23,"c":4,"d":5}
list = [1,2,3,4,6,7,8,9]

# for i,value in enumerate(list):
#     print(i+1, value)

[print(num, end =" ") for num in list]