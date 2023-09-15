
import nltk
from nltk.util import ngrams
from collections import defaultdict

# Sample text data (you can replace this with your own dataset)
text = "This is a sample text. You can replace this with your own data for training."

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Specify the N-gram order (e.g., 2 for bigrams)
n = 2

# Create an N-gram model
ngram_model = defaultdict(list)
for ngram in ngrams(words, n):
    prefix = tuple(ngram[:-1])
    next_word = ngram[-1]
    ngram_model[prefix].append(next_word)

# Function to predict the next word
def predict_next_word(prefix):
    if prefix in ngram_model:
        return max(set(ngram_model[prefix]), key=ngram_model[prefix].count)
    else:
        return "Not in model"

# Input a prefix to get the next word prediction
input_prefix = ("replace", "this")
next_word_prediction = predict_next_word(input_prefix)

# Print the prediction
print(f"Input Prefix: {' '.join(input_prefix)}")
print(f"Predicted Next Word: {next_word_prediction}")
