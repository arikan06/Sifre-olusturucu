import random

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters= [letter.upper() for letter in lower_letters]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolls=['*', "'", '"', '!', '#', '$', '+', '%', '&', '/', '{', '}', '(', ')', '[', ']', '=', '?', '-', '_', '-', '<', '>', '|', '.', ',', ':', ';', '~', '^', '´', '`']

password_formula = lower_letters + upper_letters + numbers + symbolls

def main():
    print("This program is local, your passwords will not be saved in your computer or sent to a third party.")
    password_number=input('How many randomized passwords do you want? ')
    password_lenght=input('How long do you want your password to be? ')
    print('-------------------------------')
    for i in range(int(password_number)):
            password = ''
            for len in range(int(password_lenght)):
                #print(password_formula)
                password += random.choice(password_formula)
            print(password)
    print('-------------------------------')

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)
            input()
