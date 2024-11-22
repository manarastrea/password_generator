import random
import string

def pass_generator(lenght: int = 10):
  alphabet = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(alphabet)for i in range (lenght))
  return password

password = pass_generator()
print(f"Generated password:{password}")
