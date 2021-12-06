class AnalysisBuilder:

    filename = 'analysis.csv'

    def __init__(self, model, model_name):
        self.model = model
        self.model_name = model_name
        self.model_filename = model_name+'-details.csv'
        self.vocab_size = len(model.word_vec)
        self.questions_answered = 0
        self.accuracy = 0

