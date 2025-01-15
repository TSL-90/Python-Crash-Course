"""Using json.dumps() and json.loads()"""

# number writer (dump)

from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)


# number reader (load)

# from pathlib import Path
# import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)


# remember me and greet user

# from pathlib import Path
# import json

def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None


def get_new_user_info(path):
    """Prompt for user information."""
    username = input("What is your name? ")
    city = input("What city do you live in? ")
    age = input("How old are you? ")

    user_dict = {
        'username': username,
        'city': city,
        'age': age,
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict


def greet_user():
    """Greet the user by name and show the details we know."""
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"I hope the weather is nice in {user_dict['city']}.")
        print(f"You don't look a day over {user_dict['age']}!")
    else:
        user_dict = get_new_user_info(path)
        message = f"We will remember your name when you return,{
            user_dict['username']}!"
        print(message)


greet_user()
