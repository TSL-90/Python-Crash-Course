from collections import Counter


def most_repeated_char(s):
    # Count occurrences of each character
    char_count = Counter(s)
    # Find the character with the maximum count
    most_common_char = max(char_count, key=char_count.get)
    return most_common_char, char_count[most_common_char]


# Test the function
string = "This is a common interview question."
char, count = most_repeated_char(string)
print(f"The most repeated character is '{char}' with {count} occurrences.")
