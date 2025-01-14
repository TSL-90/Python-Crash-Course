"""Reading file contents"""

from pathlib import Path

path = Path('text_files/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()  # strip the whitespace on the left side

print(pi_string)
print(len(pi_string))
