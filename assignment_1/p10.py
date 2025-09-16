Reverse a given string
str1 = "PYnative"
print("Original: ", str1)
str1 = '' .join(reversed(str1))
print("Reversed: ", str1)

Find the last position of a given substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Last occurrence of Emma starts at index: ", str1.rfind("Emma"))

Split a string on hyphens
str1 = "Emma-is-a-data-scientist"
splitted_strings = str1.split("-") 
for string in splitted_strings:
    print(string)

Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("Original list of sting")
print(str_list)
new_list = list(filter(None, str_list))
print("After removing empty strings")
print(new_list)

Remove special symbols / punctuation from a string
import string
str1 = "/*Jon is @developer & musician"

new_str1 = str1.translate(str.maketrans('', '', string.punctuation))
print(new_str1)

Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
only_int = "".join(item for item in str1 if item.isdigit())
print(only_int)

Find words with both alphabets and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"
words = str1.split()
result = []
for word in words:
    has_alpha = any(c.isalpha() for c in word)
    has_digit = any(c.isdigit() for c in word)
    if has_alpha and has_digit:
        result.append(word)
for word in result:
    print(word)

Replace each special symbol with # in the following string
import string
str1 = '/*Jon is @developer & musician!!'
replace_char = "#"
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)
print(str1)