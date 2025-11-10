# len() - returns the length of a string
text = "Hello, world!"
print(len(text)) # Output: 13

# replace(oldvalue, newvalue, count) - replaces a part of the string with another substring
greeting = "Hello, world!"
new_greeting = greeting.replace("world", "python")
print(new_greeting) # Output: "Hello, Python!"

# strip() - removes any whitespace (spaces, newlines) from the beginning and end of the string.
messy_text = "      Hello world!"
clean_text = messy_text.strip()
print(clean_text) # Output: "Hello world!"

data = "---example---"
cleaned_data = data.strip("-") # specifies the character to be removed
print(cleaned_data)

data = "---example--#"
cleaned_data = data.strip("-#") # specifies multiple characters to be removed
print(cleaned_data)

# join() - combines a list of strings into a single string
words = ['Hello', 'world', 'Python', 'is', 'great']
sentence = " ".join(words)
print(sentence) # Output: "Hello world Python is great"

# slicing() extracts part of a string by specifying a range of indices
text = "Hello, worldy worldy"
print(text[0:5]) # Output: "Hello"
print(text[-5:]) # Output: "world"

multi_line_string = "This is a string that is too long to fit on one line, so we continue it \
here without any breaks."
print(multi_line_string)

# Using triple single quotes
multiline_string_single = '''This is the first line.
This is the second line.
And this is the third line.'''
print(multiline_string_single)

# Using triple double quotes
multiline_string_double = """This is another multiline string.
It also spans multiple lines.
With embedded newlines."""
print(multiline_string_double)

