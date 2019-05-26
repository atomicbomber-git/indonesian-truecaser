import argparse
from nltk import sent_tokenize

def process(text):
    
    sentences = [list(sentence) for sentence in sent_tokenize(text)]
    
    for i, sentence in enumerate(sentences):
        sentence[0] = sentence[0].upper()
        sentences[i] = "".join(sentences[i])
    
    return " ".join(sentences)

def file_to_text(file):
    return "".join([line for line in file])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='''
     Menerima input berupa file teks dan menghasilkan output berupa teks serupa, 
     dengan penggunaan huruf kapital yang 
     benar sesuai dengan aturan PUBI.
    ''')
    parser.add_argument('file', metavar='file', nargs=1, type=argparse.FileType('r'), help='file teks input')
    
    args = parser.parse_args()
    file = args.file[0]

    text = file_to_text(file)
    result = process(text)

    print(result)