import pandas as pd
import csv
import os
import errno
from gensim.models import KeyedVectors


class ModelExecutor:

    def __init__(self):
        pass

    def runModel(self, model_file):
         # create output directory if does not already exist
        if not os.path.exists(os.path.dirname('output')):
            try:
                os.makedirs('output')
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        df = pd.read_csv("synonyms.csv")
        model = KeyedVectors.load_word2vec_format(model_file, binary=True)
        name = model_file.split('/')[len(model_file.split('/'))-1]
        destination = "output/" + name[0:len(name)-3] + '-details.csv' # offset by 3 to remove the .gz
        f = open(destination, 'w', newline='')
        writer = csv.writer(f)

        for row in df.values:
            highestScore = 0
            for (index, word) in enumerate(row):
                if word in model.key_to_index and row[0] in model.key_to_index:
                    if index > 1 and model.distance(row[0], word) > highestScore:
                        highestScoreWord = word

            if row[0] not in model.key_to_index or len(list(filter(lambda x: x in model.key_to_index, row))) < 2:
                result = "guess"
            elif row[1] == highestScoreWord:
                result = "correct"
            else:
                result = "wrong"

            writer.writerow([row[0], row[1], highestScoreWord, result])
        f.close()
        return model
