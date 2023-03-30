import os

afinn_path = os.path.join(os.path.dirname(__file__), 'AFINN-111.txt')
with open(afinn_path, 'r') as f:
    afinn = dict(map(str.strip, line.split('\t')) for line in f)

# Define a function to calculate the sentiment score of a text using the AFINN lexicon
def calculate_sentiment(text):
    words = text.split()
    score = sum([int(afinn.get(word.lower(), 0)) for word in words])
    print(len(words))
    return score



text1 = "The product is very good. I liked it."

obj = calculate_sentiment(text1)
print(obj)