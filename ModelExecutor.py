import pandas as pd
import csv
from gensim.models import KeyedVectors


class ModelExecutor:

    def runModel(self, model_file):
        df = pd.read_csv("synonyms.csv")
        model = KeyedVectors.load_word2vec_format(model_file, binary=True)
        destination = model_file + 'details.csv'
        f = open(destination, 'w')
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
