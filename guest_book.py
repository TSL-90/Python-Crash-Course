"""Input the names of all the guests"""

from pathlib import Path

path = Path('text_files/guest_book.txt')

prompt = "\nHello, what is your name? "
prompt += "\nEnter 'quit' if you're the last guest. "

guest_names = []
while True:
    name = input(prompt)
    if name.lower() == 'quit':
        break

    print(f"Thank you {name} you have been added to our guest book.")
    guest_names.append(name)


# build a string where "\n" is added after each name.
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)
