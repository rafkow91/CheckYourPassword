from os.path import exists
from password_power import StrongPassword
from password_pwned import PwnedPassword

if __name__ == '__main__':
    print('Checking your passwords from file passwords.txt')
    choice = input('Do you want save safe passwords to file good_passwords.txt? [Y/n]  ->  ')
    if choice == '' or choice[0].lower() == 'y':
        mode = 'w'
        if exists('good_passwords.txt'):
            choice2 = input('Do you want add passwords to existing file? [Y/n]  ->  ')
            if choice2 == '' or choice2[0].lower() == 'y':
                mode = 'a'
    elif choice[0].lower() == 'n':
        pass
    else:
        print('I don\'t understant. I don\'t save your passwords!')


    with open('passwords.txt', mode='r') as input_file:
        good_passwords = []
        len_input_file = 0        
        for row in input_file:
            row = row.strip()
            strong = StrongPassword(row)
            pwned = PwnedPassword(row)
            
            if all([strong.validate(), pwned.validate()]):
                print(f'Password {row} is strong and not pwned!')
                good_passwords.append(row)

            len_input_file += 1

        good_passwords = set(good_passwords)
        print(good_passwords)
        if len(good_passwords) == 0:
            print('Your passwords are weaks!')
        else:
            print(f'You have {len(good_passwords)} safe {"passwords" if len(good_passwords)>1 else "password"} - it\'s {len(good_passwords)/len_input_file*100:.2f} %...')
        if mode in ['w', 'a']: 
            with open('good_passwords.txt', mode=mode) as output_file:
                for line in good_passwords:
                    output_file.write(line + '\n')

        good_passwords = None