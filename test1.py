import enchant

# Create an English dictionary
dictionary = enchant.Dict("en_US")

# Text to check
text = "Ths is a smple spell check exmple."

# Split the text into words
words = text.split()

# Check each word for spelling errors
for word in words:
    if not dictionary.check(word):
        suggestions = dictionary.suggest(word)
        if suggestions:
            print(f"Possible suggestions for '{word}': {', '.join(suggestions)}")
        else:
            print(f"Word '{word}' is not found in the dictionary.")
