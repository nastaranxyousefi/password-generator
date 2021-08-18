#This program generates random passwords.
#developer: Nastaran Yousefi

import random
import string
import os

def clear_screen():
    os.system('clear')


settings = {
    'lower' : True,
    'upper' : True,
    'symbol' : True,
    'number' : True,
    'length' : 8
}
PASSWORD_MIN_LENGTH = 4
PASSWORD_MAX_LENGTH = 30

def checking_answer_settings(option, default):
    while True:
        user_input = input(f'Include {option}? (default is {default}),'
                        '(Enter "y" as yes, "n" as no, enter: default): ')
        if user_input == '':
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'
        print('Invalid input. Try again!')  



def get_password_length(option, default, pwd_min_len = PASSWORD_MIN_LENGTH, pwd_max_len = PASSWORD_MAX_LENGTH):
    while True:
        user_input = input('Enter password length | '
                           f'(default is {default} | enter: default) : ')
        if user_input == '':
            return default
        if user_input.isdigit():
            user_password_length = int(user_input)
            if pwd_min_len <= user_password_length <= pwd_max_len:
                return int(user_input)

            print('Invalid input.')
            print(f'password length should be between {pwd_min_len} and {pwd_max_len}.')
        else:
            print('Invalid input. you should enter a number.')
        print('Please try again!')


def get_settings_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
            user_choice = checking_answer_settings(option, default)
            settings[option] = user_choice
        else:
            user_password_length = get_password_length(option, default)
            settings[option] = user_password_length


def get_random_upper():
    return random.choice(string.ascii_uppercase)

def get_random_lower():
    return random.choice(string.ascii_lowercase)

def get_random_number():
    return str(random.randint(0,9))

def get_random_symbol():
    return random.choice("""!@#$%&*()_|][{}:;.,""")



def generate_random_char(choices):
    chosen = random.choice(choices)

    if chosen =='upper':
        return get_random_upper()
    elif chosen == 'lower':
        return get_random_lower()
    elif chosen == 'number':
        return get_random_number()
    elif chosen == 'symbol':
        return get_random_symbol()

def password_generator(settings):
    final_password = ''
    password_length =settings['length']

    choices = list(filter(lambda x:settings[x] == True, settings))

    for i in range(password_length):
        final_password += generate_random_char(choices)

    return final_password


def password_generator_loop(settings):
    while True:
        print('-' * 30)
        print(f'\nThe Generated Password : {password_generator(settings)}\n')
        while True:
            want_another_password = input('Do you want another password? (y:yes | n:no | enter:yes): ')
            if want_another_password in ['y', 'n', '']:
                if want_another_password == 'n':
                    return
                break
            print('Invalid input! Choose from (y:yes | n:no | enter:yes)')

def run():
    clear_screen()
    get_settings_from_user(settings)
    clear_screen()
    password_generator_loop(settings)
    print('Thank you for choosing us!')
    

run()
