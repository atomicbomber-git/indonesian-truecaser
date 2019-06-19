import argparse
from nltk import sent_tokenize
import re

# Memroses teks input
def process(text):
    # Memisahkan teks input menjadi kalimat
    sentences = [sentence for sentence in sent_tokenize(text)]
    result_sentences = []

    # Memroses kalimat satu per satu
    for sentence in sentences:
        # Proses teks yang terdapat didalam tanda petik
        processed = capitalize_quotation_beginning(sentence)

        # Huruf pertama pada kalimat diubah menjadi huruf besar,
        # huruf selanjutnya diubah menjadi huruf kecil
        processed = processed[0].upper() + processed[1:].lower()
        result_sentences.append(processed)

    # Gabungkan kembali teks
    return " ".join(result_sentences)


def capitalize_quotation_beginning(text):
    for phrase in re.findall('"([^"]*)"', text):
        processed_phrase = phrase.strip()
        processed_phrase = processed_phrase[0].upper() + processed_phrase[1:].lower()
        text = text.replace('{}'.format(phrase), processed_phrase)
    return text


def file_to_text(file):
    return "".join([line for line in file])


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='''
     Menerima input berupa file teks dan menghasilkan output berupa teks serupa, 
     dengan penggunaan huruf kapital yang 
     benar sesuai dengan aturan PUBI.
    ''')
    parser.add_argument('file', metavar='file', nargs=1,
                        type=argparse.FileType('r'), help='file teks input')

    args = parser.parse_args()
    file = args.file[0]

    text = file_to_text(file)

    result = process(text)
    print(result)
