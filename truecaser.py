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
    result = text

    tagged_entities = []
    
    container = ""
    is_combining = False
    
    for i, token in enumerate(tagged_text):
        token_text = token[0].lower()
        token_code = token[1][0]
        
        if (not is_combining and token_code == "B"):
            is_combining = True
            container = token_text
        elif (not is_combining and token_code == "I"):
            raise Exception()
        elif (is_combining and token_code == "B"):
            tagged_entities.append(container)
            container = token_text
        elif (is_combining and token_code == "I"):
            container += (" " + token_text)

        if (i == (len(tagged_text) - 1)):
            tagged_entities.append(container)

    print(tagged_text, end="\n\n")
    print(tagged_entities)

    for entity in tagged_entities:
        lowercased_entity = entity.lower()
        if (lowercased_entity in entity_capitalizations):
            result = result.replace(
                lowercased_entity,
                entity_capitalizations[lowercased_entity]["text"]
            )

    return result

def capitalize_quotation_beginning(text):
    # 06: Mengkapitalisasikan setiap huruf pada awal kalimat dalam tanda kutip
    for phrase in re.findall('"([^"]*)"', text):
        processed_phrase = phrase.strip()
        processed_phrase = processed_phrase[0].upper() + processed_phrase[1:]
        text = text.replace('{}'.format(phrase), processed_phrase)

    return text


def file_to_text(file):
    return "".join([line for line in file])
