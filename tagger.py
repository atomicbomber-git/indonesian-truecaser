from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from sacremoses import MosesTokenizer
import argparse
import os

current_dir_path = os.path.dirname(os.path.realpath(__file__))
ner_model_path = os.path.join(current_dir_path, "ner-model.ser.gz")
stanford_ner_jar_path = os.path.join(current_dir_path, "resources", "stanford-ner.jar")

# Initialize tagger
tagger = StanfordNERTagger(
    ner_model_path,
    stanford_ner_jar_path,
    encoding='utf-8'
)

# 01: Memasukkan teks input
def tag(text):
    # 02: Tokenisasi teks input
    tokenizer = MosesTokenizer(lang="id")
    tokens = tokenizer.tokenize(text)
    # 03 Tagging entitas bernama
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
