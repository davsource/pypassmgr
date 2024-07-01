import hashlib
import getpass

password_manager = {}

def create_account ():
    user = input("Enter your desired username: \n")
    password = getpass.getpass("Enter your desired password: \n", stream=None)

    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    password_manager[user] = hashed_pass

    print("Account created successfully!")


def login():
    user = input("Enter your username: \n")
    password = getpass.getpass("Enter your password: \n")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if user in password_manager.keys() and password_manager[user] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit.\n")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()