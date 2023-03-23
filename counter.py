import string

def count_words(filename):
    """Count the frequency of each word in the specified text file"""
    
    with open(filename, "r") as file:
        text = file.read()

    
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()

    
    words = text.split()
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    return word_counts


filename = "example.txt"
word_counts = count_words(filename)
for word, count in word_counts.items():
    print(word, count)
