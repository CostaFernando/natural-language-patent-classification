import os
import json
import csv
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    username=os.environ['NATURAL_LANGUAGE_CLASSIFIER_USERNAME'],
    password=os.environ['NATURAL_LANGUAGE_CLASSIFIER_PASSWORD']
)

def truncateAbstractText(text):
    characterLimit= 1024
    if len(text) > characterLimit:
        return text[0:characterLimit]
    else:
        return text

def writePatentsClassificationsFileHeaders(patentsClassificationsWriter):
    patentsClassificationsWriter.writerow(['patent_number', 'abstract', 'classification'])

def skipFileFirstLine(file):
    file.readline()

if __name__ == "__main__":
    print('Inicializando as classificações de patentes...')

    with open('patents_abstracts.csv', newline='') as patentsAbstractsFile, open('patents_classifications.csv', 'w', newline='') as patentsClassificationsFile:

        patentsAbstractsReader= csv.reader(patentsAbstractsFile, delimiter=",", quotechar="'")
        patentsClassificationsWriter= csv.writer(patentsClassificationsFile, delimiter=",", quotechar="'")

        writePatentsClassificationsFileHeaders(patentsClassificationsWriter)

        skipFileFirstLine(patentsAbstractsFile)
        npatent=0
        for row in patentsAbstractsReader:
            patentNumber= row[0]
            abstractText= row[1]
            npatent+= 1
            print('Classificando ' + npatent + 'ª patente...')
            classes= natural_language_classifier.classify(os.environ['NATURAL_LANGUAGE_CLASSIFIER_CLASSIFIER_ID'],
                truncateAbstractText(abstractText))
            patentsClassificationsWriter.writerow([patentNumber, abstractText, classes['top_class']])

    print('Patentes classificadas com sucesso!')
