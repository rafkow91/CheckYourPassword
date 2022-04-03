""" App to check strong and leaks you passwords
    Args:
        passwords.txt: passwords from this file will be checking

    Returns:
        good_passwords.txt: in this file will be saving (if you want it)
            strong and not leaks passwords

"""
from os.path import exists
from password_power import StrongPassword
from password_pwned import PwnedPassword

if __name__ == '__main__':
    print('Checking your passwords from file passwords.txt')
    choice = input('Do you want save safe passwords to file good_passwords.txt? [Y/n]  ->  ')
    if choice == '' or choice[0].lower() == 'y':
        MODE = 'w'
        if exists('good_passwords.txt'):
            choice2 = input('Do you want add passwords to existing file? [Y/n]  ->  ')
            if choice2 == '' or choice2[0].lower() == 'y':
                MODE = 'a'
    elif choice[0].lower() == 'n':
        pass
    else:
        print('I don\'t understant. I don\'t save your passwords!')

    with open('passwords.txt', mode='r', encoding='utf8') as input_file:
        GOOD_PASSWORDS = []
        INPUT_PASSWORDS = set()
        for row in input_file:
            row = row.strip()
            strong = StrongPassword(row)
            pwned = PwnedPassword(row)
            if all([strong.validate(), pwned.validate()]):
                GOOD_PASSWORDS.append(row)
            INPUT_PASSWORDS.add(row)

        GOOD_PASSWORDS = set(GOOD_PASSWORDS)

        if len(GOOD_PASSWORDS) == 0:
            print('Your passwords are weaks!')
        else:
            print(f'You have {len(GOOD_PASSWORDS)} safe \
{"passwords" if len(GOOD_PASSWORDS)>1 else "password"} \
- it\'s {len(GOOD_PASSWORDS)/len(INPUT_PASSWORDS)*100:.2f} %...')

        if MODE in ['w', 'a']:
            with open('good_passwords.txt', mode=MODE, encoding='utf8') as output_file:
                for line in GOOD_PASSWORDS:
                    output_file.write(line + '\n')

        GOOD_PASSWORDS = None
        INPUT_PASSWORDS = None
