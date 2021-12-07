from AnalysisBuilder import AnalysisBuilder
from ModelExecutor import ModelExecutor


model_executor = ModelExecutor()
twitter_model_100 = model_executor.runModel('glove-twitter-100', binary=False)
wiki_model_100 = model_executor.runModel('glove-wiki-gigaword-100', binary=False)
wiki_model_50 = model_executor.runModel('glove-wiki-gigaword-50', binary=False)
wiki_model_200 = model_executor.runModel('glove-wiki-gigaword-200', binary=False)

analyzer = AnalysisBuilder()
analyzer.writeAnalysis(twitter_model_100, 'glove-twitter-100')
analyzer.writeAnalysis(wiki_model_100, 'glove-wiki-gigaword-100')
analyzer.writeAnalysis(wiki_model_50, 'glove-wiki-gigaword-50')
analyzer.writeAnalysis(wiki_model_200, 'glove-wiki-gigaword-200')

