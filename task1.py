
from AnalysisBuilder import AnalysisBuilder
from ModelExecutor import ModelExecutor

model_executor = ModelExecutor()
google_model_300 = model_executor.runModel('models/word2vec-google-news-300.gz')


analyzer = AnalysisBuilder()

analyzer.writeAnalysis(google_model_300, 'word2vec-google-news-300')






