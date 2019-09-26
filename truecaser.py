import argparse
from nltk import sent_tokenize
import re
from tagger import tag
from sacremoses import MosesDetokenizer
import json
import os

# Memroses teks input
def process(text):
    # Memisahkan teks input menjadi kalimat
    sentences = [sentence for sentence in sent_tokenize(text)]
    result_sentences = []

    # Memroses kalimat satu per satu
    for sentence in sentences:
        processed = capitalize_named_entities(sentence)

        # Proses teks yang terdapat didalam tanda kutip
        processed = capitalize_quotation_beginning(processed)

        # 05: Mengkapitalisasikan setiap huruf pada awal kalimat
        # Huruf pertama pada kalimat diubah menjadi huruf besar,
        # huruf selanjutnya diubah menjadi huruf kecil
        processed = processed[0].upper() + processed[1:]
        result_sentences.append(processed)

    # 07: Menampilan teks yang perlu diproses
    return " ".join(result_sentences)

def capitalize_named_entities(text):
    # 04: Mengubah penulisan entitas bernama dalam teks sesuai dengan kapitalisasi yang benar
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    entity_capitalizations = json.loads(open(os.path.join(current_dir_path, "entity_capitalizations.json")).read())

    tagged_text = tag(text)
    result = []
    for token in tagged_text:
        if (token[0].lower() in entity_capitalizations):
            result.append(entity_capitalizations[token[0].lower()])
        else:
            result.append(token[0])

    detokenizer = MosesDetokenizer(lang="id")
    return detokenizer.detokenize(result)

def capitalize_quotation_beginning(text):
    # 06: Mengkapitalisasikan setiap huruf pada awal kalimat dalam tanda kutip
    for phrase in re.findall('"([^"]*)"', text):
        processed_phrase = phrase.strip()
        processed_phrase = processed_phrase[0].upper() + processed_phrase[1:]
        text = text.replace('{}'.format(phrase), processed_phrase)

    return text


def file_to_text(file):
    return "".join([line for line in file])
