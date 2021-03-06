import pandas as pd
import os
import errno
import csv


class AnalysisBuilder:

    def __init__(self):
        pass

    destination = 'output/analysis.csv'

    def writeAnalysis(self, model, model_name):
        """
        Given the model and model name,
        calculates/determines the following information and outputs it to an analysis.csv file:

        (a) the model name (clearly indicating the source of the corpus and the vector size)
        (b) the size of the vocabulary (the number of unique words in the corpus1)
        (c) the number of correct labels
        (d) the number of questions that your model answered without guessing
        (e) the accuracy of the model (i.e. (c)/(d))

        :return:
        """

        # create output directory if does not already exist
        if not os.path.exists(os.path.dirname('output')):
            try:
                os.makedirs('output')
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        # read from the model's details csv (created by the Model Executor)
        model_filename = 'output/' + model_name + '-details.csv'
        df = pd.read_csv(model_filename)
        f = open(self.destination, 'a+', newline='')
        writer = csv.writer(f)

        vocab_size = len(model.index_to_key)
        correct = 0
        questions_answered = 0

        for row in df.values:
            if row[3] == 'correct':
                correct += 1

            if row[3] != 'guess':
                questions_answered += 1

        if questions_answered == 0:
            accuracy = 0
        else:
            accuracy = correct/questions_answered
        writer.writerow([model_name, vocab_size, correct, questions_answered, accuracy])
        f.close()
