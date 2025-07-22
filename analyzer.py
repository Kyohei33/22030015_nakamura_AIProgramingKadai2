from janome.tokenizer import Tokenizer
import pandas as pd
from collections import Counter

def tokenize(text):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)
    return tokens

def extract_words(tokens, pos_list=["名詞", "動詞", "形容詞"]):
    words = [token.surface for token in tokens if token.part_of_speech.split(',')[0] in pos_list]
    return words

def count_words(words):
    return Counter(words)

def analyze_text(text):
    tokens = tokenize(text)
    words = extract_words(tokens)
    counter = count_words(words)
    df = pd.DataFrame(counter.items(), columns=["単語", "出現回数"]).sort_values(by="出現回数", ascending=False)
    return df.reset_index(drop=True)

def analyze_file(text):
    return analyze_text(text)
