import string
import random

if __name__ == '__main__':
    # s1 = string.ascii_letters
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.ascii_lowercase
    # print(s3)
    s4 = string.digits
    # print(s4)
    s5 = string.punctuation
    # print(s5)
    while True:
        try:
            plen = int(input("Enter password length: "))
            break
        except ValueError:
            print("Oops! Enter a valid number")
    s = []
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))
    # print(s)
    # random.shuffle(s)
    # print(s)
    print("Your password is: ", end="")
    print("".join(random.sample(s, plen)))
    # print("".join(s[0:plen]))
    
