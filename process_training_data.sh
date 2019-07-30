#!/bin/sh

OUTPUT_FILE=training.tsv

rm $OUTPUT_FILE
./process_training_data.py data_test.txt >> $OUTPUT_FILE
# ./process_training_data.py training_data.txt >> $OUTPUT_FILE

java -cp ./resources/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop indonesian.prop