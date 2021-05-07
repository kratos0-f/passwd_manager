import random

capitalized_letter = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower_case = capitalized_letter.lower()
special_simbols = "!@#_()"
numbers = "123456789"

def set_symbols():      # create string of symbols
    print("1 - capitalized letter \n 2 - lower case \n 3 - special symbols \n 4 - numbers")
    set_1 = list(input())
    result = ""
    if "1" in set_1:
        result += capitalized_letter
    if "2" in set_1:
        result += lower_case
    if "3" in set_1:
        result += special_simbols
    if "4" in set_1:
        result += numbers
    
    return result

def password_generator(symbols):
    print("ENTER count of characters: \n")
    count = int(input())
    result = ""
    for i in range(count):
        result += symbols[random.randrange(0, len(symbols))]
    
    return result

set_symbols = set_symbols()
passwd = password_generator(set_symbols)
print(passwd)