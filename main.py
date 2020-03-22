def welcome():
    welcome = input('Welcome! Would you like to login or register? ')

    if welcome == 'login':
        login()
    if welcome == 'register':
        register()

def login():
    enteredusername = input('Please enter your username. ')

    with open(f'{enteredusername}', 'rt') as credentials:
      file_content = credentials.readline()
      username = file_content.split(';')[0]
      enteredpassword = input(f'Welcome {username} please enter your password. ')
      password = file_content.split(';')[1]

      if enteredpassword == password:
          loginsuccessful()
      if enteredpassword != password:
          print('The password you entered is incorrect.')

def register():
    username = input('Great! What would you like to be called? ')
    password = input(f'Welcome {username}, please enter a password to get into your account (Password must be > 8 characters). ')

    if len(password) < 8:
        password = input('Sorry! Your password must be longer than 8 characters. ')

    credentials = open(f'{username}.', 'a+')
    credentials.write(f'{username};{password}')
    credentials.close()

    welcome()

def loginsuccessful():
    print('So, your in. What are you going to do now?')
    input('')

if __name__ == '__main__':
    welcome()