"""Reading file contents"""

from pathlib import Path

path = Path('text_files/pi_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()  # strip the whitespace on the left side

print(pi_string)
print(len(pi_string))

# Writing to a file

path = Path('text_files/programming.txt')
path.write_text("I love programming.")

# Writing multiple lines to a file.
# from pathlib import Path
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('text_files/programming.txt')
path.write_text(contents)


# 10-4 Guest
# from pathlib import Path
path = Path('text_files/guest.txt')
guest = input('Please write your here for our guest book: ')

path.write_text(guest)
