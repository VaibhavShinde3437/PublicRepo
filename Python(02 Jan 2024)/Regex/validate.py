import re

# email = input("What's your email? ").strip()
# if '@' in email and '.' in email:
#     print("Valid")
# else:
#     print("Invalid")

# =========================================================================================================================================================

# email = input("What's your email? ").strip()
# username, domain = email.split("@")
# if username and domain.endswith(".com"):
#     print("Valid")
# else:
#     print("Invalid")

# ==========================================================================================================================================================

# import re
# email = input("What's your email? ").strip()
# if re.search("@",email):
#     print("Valid")
# else:
#     print("Invalid")

# =========================================================================================================================================================

# email = input("What's your email? ").strip()
# if re.search(".+@.+",email):
#     print("Valid")
# else:
#     print("Invalid")

# =========================================================================================================================================================

# email = input("What's your email? ").strip()
# if re.search(r".+@.*\.com",email):
#     print("Valid")
# else:
#     print("Invalid")

# ========================================================================================================================================================

# email = input("What's your email? ").strip()
# if re.search(r"^.+@.*\.com$",email):
#     print("Valid")
# else:
#     print("Invalid")

# ========================================================================================================================================================

# email = input("What's your email? ").strip()
# if re.search(r"^[^@]+@[^@]+\.com$",email):
#     print("Valid")
# else:
#     print("Invalid")

# ========================================================================================================================================================

# email = input("What's your email? ").strip()
# if re.search(r"^[a-z0-9]+@[a-z0-9]+\.com$",email):
#     print("Valid")
# else:
#     print("Invalid")

# =======================================================================================================================================================

# email = input("What's your email? ").strip()
# if re.search(r"^\w+@\w+\.com$",email):
#     print("Valid")
# else:
#     print("Invalid")

# =======================================================================================================================================================

# email = input("What's your email? ").strip()
# if re.search(r"^\w+@\w+(.com|.edu|.org|.in)$",email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")

# =======================================================================================================================================================

email = input("What's your email? ").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.com$",email):
    print("Valid")
else:
    print("Invalid") 