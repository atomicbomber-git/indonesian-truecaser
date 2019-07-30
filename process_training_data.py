#!/usr/bin/python3

import nltk
import sys
from html.parser import HTMLParser
from nltk.tokenize import word_tokenize

conversion_table = {}
conversion_table_file = open("conversion_table.tsv", "w")

class CustomHTMLParser(HTMLParser):
    def __init__(self, convert_charrefs=True):
        super().__init__(convert_charrefs=True)
        self.tag = None

    def handle_starttag(self, tag, attrs):
        self.tag = tag.upper()

    def handle_endtag(self, tag):
        self.tag = None
        # print(tag.upper())

    def handle_data(self, data):
        lowercased = data.lower()
        tokens = word_tokenize(lowercased)

        if (self.tag != None):
            for i, token in enumerate(tokens):
                if self.tag in ["ORGANIZATION", "PERSON"]:
                    conversion_table[token] = data

                prefix = "I"
                if i == 0:
                    prefix = "B"

                print("{} {}-{}".format(token, prefix, self.tag.upper()))
        else:
            for token in tokens:
                if not token.isalpha():
                    continue
                print(token, end=" O\n")

# Download NLTK data, which is required for nltk.word_tokenize and some other functions
nltk.download("punkt", quiet=True)

if len(sys.argv) < 2:
    print("Program ini memerlukan minimal 1 argumen yang berisi nama file yang hendak diproses.")
    exit(1)

filename = sys.argv[1]

parser = CustomHTMLParser()
with open(filename) as file:
    for line in file:
        parser.feed(line)

for key, value in conversion_table.items():
    print("{} {}".format(key, value), file=conversion_table_file)