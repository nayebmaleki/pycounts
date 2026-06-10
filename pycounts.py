"""
python -c ”import this” > zen.txt
sudo apt install cookiecutter
"""

from collections import Counter
from string import punctuation

"""
print(punctuation)  #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

words = ["a", "happy", "hello", "a", "world", "happy"]
word_counts = Counter(words)
#print(word_counts)   #Counter({'a': 2, 'happy': 2, 'hello': 1, 'world': 1})

with open("zen.txt",encoding="utf-16") as file:
    text = file.read()



text = text.lower()
for p in punctuation:
    text = text.replace(p, "")
text =text.split()
print(text) 
word_counts = Counter(text)
print(word_counts)
"""

def load_text(input_file):
    """Load text from a text file and return as a string."""
    with open(input_file, "r",encoding="utf-16") as file:
        text = file.read()
    return text

def clean_text(text):
    """Lowercase and remove punctuation from a string."""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text

def count_words(input_file):
    """Count unique words in a string."""
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)

if __name__ == "__main__":
    word_counts = count_words("zen.txt")
    print(word_counts)  
