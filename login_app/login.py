# Simulates a simple login prompt
# Requirements
#    * Duplicate usernames are not allowed.
#    * If a username / password match is not found the user should be told
#    * If a match is not found the user should asked if they want to try again
#    * When a new entry is added it must be persistent across restarts
#    * If a username password match is found the user should be allowed to login


# Validate the username
# Clear the screen
# Prompt for username
# Prompt for password

usernames = ['bob']

def login_greeting() -> str:
    return "Hello, welcome to Tomorrow. Please log in..."

def is_valid_username(username: str, usernames: list[str]) -> bool:
    if not username: raise ValueError("Username cannot be null")
    uname_list = (u.lower() for u in usernames)
    return username.lower() not in uname_list

def is_valid_password(password: str) -> bool:
    ''' Must have:
        * 1 letter
        * 1 number
        * 1 special character
        * 8 characters minimum
    '''
    if not password: raise ValueError("Password cannot be null")

    

def username_prompt() -> str:
    return input("Username: ")

def password_prompt() -> str:
    return input("Password: ")

def login():
    login_greeting()
    username = username_prompt()
    password = password_prompt()


def main():
    print("test")

if __name__=='__main__':
    main()
