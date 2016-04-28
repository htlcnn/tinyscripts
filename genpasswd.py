import string
import random

def gen_passwd(length=16):
    result = []
    result.append(random.choice(string.ascii_lowercase))
    result.append(random.choice(string.ascii_uppercase))
    result.append(random.choice(string.digits))
    result.append(random.choice(string.punctuation))
    for i in range(length-len(result)):
        result.append(random.choice(string.printable))
    random.shuffle(result)
    return ''.join(result)


if __name__ == "__main__":
    gen_passwd()
