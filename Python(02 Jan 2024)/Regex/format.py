import re

# name = input("What's your name? ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"Hello, {name}")

# ========================================================================================================================================================

# name = input("What's your name? ").strip()
# matches = re.search("^(\w+), *(\w+)$",name)
# if matches:
#     last, first = matches.groups()
#     name = f"{first} {last}"
# print(f"Hello, {name}")

# =======================================================================================================================================================

# name = input("What's your name? ").strip()
# matches = re.search("^(\w+), *(\w+)$",name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"Hello, {name}")

# ======================================================================================================================================================

# name = input("What's your name? ").strip()
# if matches := re.search("^(\w+), *(\w+)$",name):
#     name = matches.group(2) + " " + matches.group(1)
# print(f"Hello, {name}")

# =====================================================================================================================================================

# url = input("Url : ")

# username = url.removeprefix("https://instagram.com/")
# print("Username :", username)

# =====================================================================================================================================================

url = input("Url : ")
matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$",url)
if matches:
    username = matches.group(1)
    print("Username :", username)


