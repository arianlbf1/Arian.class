from bcrypt import *

salt = gensalt(rounds=5, prefix=b"2a")
print(salt)
print(len(salt))