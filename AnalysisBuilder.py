import pandas as pd
import csv


class AnalysisBuilder:

    destination = 'analysis.csv'

    def __init__(self, model, model_name):
        self.model = model
        self.model_name = model_name
        self.model_filename = model_name+'-details.csv'

    def writeAnalysis(self):
        df = pd.read_csv(self.model_filename + '-details.csv')
        f = open(self.destination, 'a+', newline='')
        writer = csv.writer(f)

        for row in df.values:
            vocab_size = len(self.model)
            correct = 0
            questions_answered = 0

            if row[3] == 'correct':
                correct += 1

            if row[3] != 'guess':
                questions_answered += 0

        accuracy = correct/questions_answered
        writer.writerow([self.model_name, vocab_size, correct, questions_answered, accuracy])
        f.close()

