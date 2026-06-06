import random
import string

a = random.choice(string.ascii_uppercase)
b = random.choice(string.ascii_lowercase)
c = random.choice(string.digits)
d = random.choice(string.punctuation)

all = string.ascii_letters + string.digits + string.punctuation
arr = [random.choice(all) for _ in range(4)]

res = list(a + b + c + d) + arr
random.shuffle(res)
print("".join(res))

