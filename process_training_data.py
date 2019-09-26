#!/usr/bin/python3

import nltk
import sys
import json
from html.parser import HTMLParser
from nltk.tokenize import word_tokenize

tags = ["ORGANIZATION", "PERSON"]
conversion_table_filename = "entity_capitalizations.json"
raw_training_filename = "data_train.txt"
training_filename = "training.tsv"
separator = "\t"

conversion_table = {}
conversion_table_file = open(conversion_table_filename, "w")
training_file = open(training_filename, "w")

class CustomHTMLParser(HTMLParser):
    def __init__(self, convert_charrefs=True):
        super().__init__(convert_charrefs=True)
        self.tag = None

    def handle_starttag(self, tag, attrs):
        self.tag = tag.upper()

    def handle_endtag(self, tag):
        self.tag = None

    def handle_data(self, data):
        lowercased = data.lower()
        tokens = word_tokenize(lowercased)

        if (self.tag != None):

            conversion_table[data.lower()] = {
                "text": data,
                "type": self.tag,
            }

            for i, token in enumerate(tokens):
                if self.tag in tags:
                    prefix = "I"
                if i == 0:
                    prefix = "B"

                print("{}{}{}-{}".format(token, separator, prefix, self.tag.upper()), file=training_file)
        else:
            for token in tokens:
                if not token.isalpha():
                    continue
                print("{}{}O".format(token, separator), file=training_file)

nltk.download("punkt", quiet=True)

def run():
    parser = CustomHTMLParser()
    with open(raw_training_filename) as file:
        for line in file:
            parser.feed(line)

    json.dump(conversion_table, conversion_table_file, indent=True)

    conversion_table_file.close()
    training_file.close()