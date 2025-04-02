# str.lower()
The str.lower() method converts all uppercase characters in a string to lowercase, leaving other characters unchanged. This method is particularly useful for case-insensitive operations.
# str.upper()
The str.upper() method converts all lowercase characters in a string to uppercase , while leaving other characters unaffected. This is often used for emphasis or standardization in outputs.
# str.title()  
Converts the first character of each word to uppercase and all others to lowercase. Words are separated by whitespace or punctuation.
# str.capitalize()
Capitalizes only the first character of the string and lowercases all others.
# str.swapcase()
Inverts the case of each character in the string.
# str.index()
The str.index() method in Python returns the index of the first occurrence of a specified substring in a string. If the substring is not found,it raises a ValueError.
# str.find()
The str.find() method in Python locates the first occurrence of a substring in a string. It returns the index if found, or -1 if not, making it safer than str.index().
# str.startswith()
This method in Python is used to check if a string starts with a specified prefix (substring). It returns True if the string begins with the given prefix, and False otherwise.
# str.count()
This method counts the number of non-overlapping occurrences of a substring in a string.
# str.endswith()
This method checks if a string ends with a specified suffix and returns True or False.
# str.replace()
This method replaces all occurrences of a specified substring with another substring.
# str.strip()
Removes leading and trailing characters (whitespace by default) from the string.
# str.lstrip()
Removes leading characters (whitespace by default) from the string.
# str.rstrip()
Removes trailing characters (whitespace by default) from the string.
# str.split()
This method splits a string into a list of substrings based on a specified delimiter.
# str.join()
This method joins elements of a list (or iterable) into a single string, using the string it is called on as a separator.
# str.isalpha()
This checks if all characters in a string are alphabetic (letters only). It returns True or False.
# str.isdigit()
This checks whether all characters in the string are numeric digits. If they are, it returns True; otherwise, it returns False.
# str.isspace()
 checks whether all characters in the string are whitespace characters (like spaces, tabs, or newlines). It returns True if they are; otherwise, it returns False.
 # str.isalnum()
 This method checks whether all characters in the string are alphanumeric (letters or numbers, but no spaces or special characters). If they are, it returns True; otherwise, it returns False.
 # str.format()
 A method to format strings in Python. It allows inserting variables into strings using curly braces {}.
# f-strings
Introduced in Python 3.6, these provide a more concise way to format strings. Prefix the string with an f and insert variables or expressions inside curly braces {}.F-strings are generally preferred for their readability and efficiency.
# len()
A built-in function that returns the length of an object. For strings, it gives the number of characters.
# str.encode()
This method is used to encode a string into bytes. By default, it uses UTF-8 encoding unless you specify another encoding. It's useful for preparing strings for tasks like data transmission or storage, where byte representation is required.
# st.isupper()
This checks whether all the alphabetic characters in the string are uppercase. Similar to islower(), it returns False for empty strings or strings with non-alphabetic characters.
# str,islower()
This checks whether all the alphabetic characters in the string are lowercase. If the string is empty or contains non-alphabetic characters, it still returns False.