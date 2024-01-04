# class Test:
#     pass
# print(type(Test()))
# print(type(Test))

# =========================================================================================================================================================

# Test = type('Test', (), {"x" : 100})

# t = Test()
# print(t.x)
# t.y = 200
# print(t.y)

# ==========================================================================================================================================================

# class Hello:
#     def greeting(self):
#         print("Hello")

# def say(self):
#     self.x = 100

# Test = type('Test', (Hello, ), {"x" : 100, "saying": say})
# test = Test()
# test.saying()
# print(test.x)

# =======================================================================================================================================================

class Meta(type):
    pass

class Test(metaclass = Meta):
    pass

print(Test())
print(type(Test))
print(type(Meta))