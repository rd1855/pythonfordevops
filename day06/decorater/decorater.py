# ===============================
# Decorators
# ===============================

# Decorator to convert output to uppercase
def convert_upper(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

# Decorator to remove commas from output
def remove_punctuation(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).replace(",", "")
    return wrapper

# ===============================
# Example 1: Uppercase a word
# ===============================
@convert_upper
def show_word(word):
    return word

print(show_word("hello"))          # Output: HELLO
print(show_word("hello world"))    # Output: HELLO WORLD

# ===============================
# Example 2: Remove punctuation from a sentence input
# ===============================
@remove_punctuation
def take_sentence():
    sentence = input("Enter a sentence: ")
    return sentence

print(take_sentence())             # Input: Hello, world! Output: Hello world!

# ===============================
# Example 3: Stack decorators
# ===============================
@convert_upper
@remove_punctuation
def take_sentence_upper():
    sentence = input("Enter a sentence: ")
    return sentence

print(take_sentence_upper())       # Input: Hello, world! Output: HELLO WORLD
