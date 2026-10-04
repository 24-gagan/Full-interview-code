import random
import string
def generate_password():
    print("=====Strong password=====")
    try:
        length=int(input("Enter length of password:"))
        if length<6:
            print("length of password must be 6")
            return
    except ValueError:
        print("Invalid input please enter a number")
        return
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation
    password=[random.choice(lowercase),random.choice(uppercase),
              random.choice(digits),random.choice(symbols)
              ]
    all_chars=lowercase+uppercase+digits+symbols
    password+=random.choice(all_chars,k=length-4)
    random.shuffle(password)
    final_password="".join(password)
    print("Your generated password",final_password)
generate_password()