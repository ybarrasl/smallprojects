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
    specials = ["!","@","#","$","%","&","*","(",")","_","-","=","+"]
    conditions = {
        "uppercase": lambda pwd: any(x.isupper() for x in pwd),
        "lowercase": lambda pwd: any(x.islower() for x in pwd),
        "number": lambda pwd: any(x.isdigit() for x in pwd),
        "special": lambda pwd: any(x in specials for x in pwd),
        "length": lambda pwd: len(pwd) >= 8
    }

    if not password: 
        raise ValueError("Password cannot be null")

    for name, condition in conditions.items():
        if not condition(pwd=password):
            raise ValueError(f"Invalid Password, lacking: {name}")

    return True
    
def is_valid_login(username: str, password: str) -> bool:
    try:
        is_valid_username(username=username)
        is_valid_password(password=password)
        return True
    except ValueError as error:
        print(f'Invalid Credentials: {error}')
        return False
    

def username_prompt() -> str:
    return input("Username: ")

def password_prompt() -> str:
    return input("Password: ")

def create_login():
    ''' when a new account is needed '''
    login_greeting()
    username = username_prompt()
    password = password_prompt()

def login():
    '''for users that have already created an account'''

def main():
    login_path = input('Would you like to login or create a new account?')
    print("test")

if __name__=='__main__':
    main()
