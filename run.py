from user import user
from password import password

def create_user(firstname, lastname,username, password):
    return user

def save_user (user):
    user.save.user()

def find_user(username):
     return user.find_by_username(username)

def display_user():
    return user.display_user()  

def delete_user(user):
   user.delete_user() 

def create_accountname(accountname, password):
    password = Password(accountname, password)
    return password
 
def save_accountname(accountname):
        passwords.save_accountname()

def find_accountname(accountname):
    return accountname.find_by_accountname(accountname)

def find_password(accountname):
     return password().find_by_accountname(accountname)
     
def delete_accountname(password):
    password.delete_password() 



def main():
    print("Hello,Welcome")
    print("To move smoothly pick the correct coresponding number according  to how it appears")
    while True:
        print(" 1) Log In \n 2) Sign Up \n 3) Your account Information \n 4) Log Out")

        choice = int(input())
        if choice == 1:
            print("Enter your username")
            username = input()
            print("Enter your password")
            password = input()
            user = find_user(username)
            if user.username == username and user.password == password:
    
                print('Login')
                while True:

                    print(
                        f'Welcome {username}, to Password Locker to continue select the corresponding number ')

                    print(
                        ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                    log_choice = int(input())
                    if log_choice == 1:
                        print('New page')
                        print('*'*100)

                        print('Page name')
                        accountname= input()

                        print('password')
                        password = input()

                    # created and saved page
                        save_accountname(create_accountname(accountname, password))

                    elif log_choice == 2:
                        print("Enter the account name that you want to delete")

                        page = input()
                        if isexist_accountname(accountname):
                            remove_accountname= (accountname)
                            delete_accountname(remove_accountname)

                        else:
                            print(f'Invalid {accountname}')

                    elif log_choice == 3:
                        if display_accountname():
                            for pag in display_accountname():
                                print(
                                    f'{pag.accountname}:{pag.password}'
                                )
                        else:
                            print('Your Password is Invalid')
                            print('\n')

                    elif log_choice == 4:
                        print('OOPS')
                        break
                    else:
                        print('Your account cant be find')

        if choice == 2:
            print('ACCOUNT')
            print('*'*60)

            print('FIRSTNAME')
            firstname = input()

            print('LASTNAME')
            lastname = input()

            print('USERNAME')
            username = input()

            print('PASSWORD')
            password = input()

            save_user(create_user(
                firstname, lastname, username, password))
        
            print('THANK YOU YOUR ACCOUNT HAS BEEN CREATED SUCCESSFUL')
            while True:

                print(
                    f'Welcome {username},')
                print(
                    ' 1) Save new password \n 2) Delete password')

                log_choice = int(input())
                if log_choice == 1:
                    print('New accountname')
                    print('*'*100)

                    print('accountname name')
                    accountname = input()

                    print('password')
                    password = input()

                    save_accountname(create_accountname(accountname, password))

                elif log_choice == 2:
                    print("Enter the username you want to delete")

                    accountname= input()
                    if isexist_accountname(accountname):
                        remove_accountname = (accountname)
                        delete_accountname(remove_accountname)

                    else:
                        print(f'I cant find {accountname}')
                        break

    
if __name__ == '__main__':
    main()

         