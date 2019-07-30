from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from sacremoses import MosesTokenizer
import argparse

# Initialize tagger
tagger = StanfordNERTagger(
    "./ner-model.ser.gz",
    "./resources/stanford-ner.jar",
    encoding='utf-8'
)

def tag(text):
    tokenizer = MosesTokenizer(lang="id")
    tokens = tokenizer.tokenize(text)
    return tagger.tag(tokens)

if __name__ == "__main__":
    # Parse command line arguments
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "text",
        help="Teks yang hendak diproses dengan tagger NER",
    )
    arguments = argument_parser.parse_args()

    print(tag(arguments.text))
