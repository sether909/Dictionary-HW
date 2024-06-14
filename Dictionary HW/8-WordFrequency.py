import os 
import string

def word_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read()

    # Remove punctuation using str.translate and str.maketrans
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    words = text.split()
    frequency = {}

    for word in words:
        word = word.lower()  # Convert 
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    for word, count in frequency.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    word_frequency('sometext-1.txt')
