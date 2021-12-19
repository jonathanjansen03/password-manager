import random
import secrets
import string
import encryption

def generate_password():
    n = random.randint(8, 15)
    chars = string.ascii_letters + string.digits

    return ''.join(secrets.choice(chars) for i in range(n))

def input_credentials():
    app = input("What will it be used for?\n")
    username = input("Input username/email: ")

    while(True):
        choice = input("Would you like your password to be randomly generated? (Yes | No) ").lower()

        if choice == "yes":
            password = generate_password()
            print(f"Your password is: {password}")
            break
        elif choice == "no":
            password = input("Input password: ")
            break
        else:
            input("Please enter a valid option!")
        
    return app, username, password

def encrypt_credentials(app, username, password):
    app = encryption.encrypt(app)
    username = encryption.encrypt(username)
    password = encryption.encrypt(password)

    return app, username, password

def decrypt_credentials(app, username, password):
    app = encryption.decrypt(app)
    username = encryption.decrypt(username)
    password = encryption.decrypt(password)

    return app, username, password

def save_credentials(app, username, password):
    file = open("Password Manager\credentials.txt", "a")

    file.write(f"{app}#{username}#{password}\n")

if __name__ == "__main__":
    app, username, password = input_credentials()

    print(f"\n{app} Account")
    print(f"Username/email: {username}")
    print(f"Password: {password}")

    save_credentials(app, username, password)

    print("\nYour credentials are saved!")
    input("Press ENTER to close the program")