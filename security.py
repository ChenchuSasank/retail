user_credentials = {'username1': 'password1', 'username2': 'password2'}

def authenticate_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_credentials and user_credentials[username] == password:
        print("Authentication successful. Welcome, {}!".format(username))
    else:
        print("Authentication failed. Incorrect username or password.")

def add_user():
    new_username = input("Enter a new username: ")
    new_password = input("Enter a new password: ")
    user_credentials[new_username] = new_password
    print("User '{}' added successfully.".format(new_username))

if __name__ == "__main__":
    print("Welcome to the secure application.")
    while True:
        print("Select an option:")
        print("1. Authenticate user")
        print("2. Add a new user")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            authenticate_user()
        elif choice == '2':
            add_user()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")