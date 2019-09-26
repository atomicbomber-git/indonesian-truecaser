import process_training_data 
import subprocess

# Langkah praproses
process_training_data.run()

# Langkah training
subprocess.check_call("java -cp ./resources/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop indonesian.prop", shell=True)