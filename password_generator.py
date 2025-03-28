import secrets
import string

'''
    0000 0000 =  1 byte = unsigned char
    Python does not use arrays, uses lists
    iterable = collection of things we can loop over
    tri except block
'''

def gen_password(length : int = 10) -> str:
   
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # alphabet_2 = []
    # for ascii in range(97,122):
    #    alphabet_2.append(chr(ascii))
    # print(alphabet_2, string.ascii_lowercase)
    password : str = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    gen_password()
    while(True):
        try:
            user_input = input('Input a length buster: ')
            print(gen_password(int(user_input)))
        except Exception as ex: 
            print("GO FUCK YOURSELF")
            print(ex)


if __name__ == "__main__":
    main();
