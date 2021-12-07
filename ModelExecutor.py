import pandas as pd
import csv
import os
import errno
from gensim.models import KeyedVectors


class ModelExecutor:

    def __init__(self):
        pass

    def runModel(self, model_name, binary=True):
        # create output directory if does not already exist
        if not os.path.exists(os.path.dirname('output')):
            try:
                os.makedirs('output')
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        df = pd.read_csv("synonyms.csv")
        destination = "output/" + model_name + '-details.csv'
        f = open(destination, 'w', newline='')
        writer = csv.writer(f)

        model = KeyedVectors.load_word2vec_format('models/' + model_name + '.gz', binary=binary)
        answer = ''

        for row in df.values:
            highestScore = 0.0
            for i in range(2, 6):
                word = row[i]
                # verify that both the word and answer are in the model's vocabulary
                if word in model.index_to_key and row[0] in model.index_to_key:
                    print(f"Similarity for {row[0]},{word} = {model.similarity(row[0], word)}")
                    if model.similarity(row[0], word) > highestScore:
                        highestScore = model.similarity(row[0], word)
                        answer = word

            if row[0] not in model.index_to_key or len(list(filter(lambda x: x in model.index_to_key, row))) < 2:
                result = "guess"
            elif row[1] == answer:
                result = "correct"
            else:
                result = "wrong"
            writer.writerow([row[0], row[1], answer, result])
        f.close()
        return model
