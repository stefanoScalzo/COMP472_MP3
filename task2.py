# %%
from AnalysisBuilder import AnalysisBuilder
from ModelExecutor import ModelExecutor


model_executor = ModelExecutor()
twitter_model_100 = model_executor.runModel('models/glove-twitter-100.gz')
wiki_model_100 = model_executor.runModel('models/glove-wiki-gigaword-100.gz')
wiki_model_50 = model_executor.runModel('models/glove-wiki-gigaword-50')
wiki_model_200 = model_executor.runModel('models/glove-wiki-gigaword-200.gz')

analyzer = AnalysisBuilder()

analyzer.writeAnalysis(twitter_model_100, 'glove-twitter-100')
analyzer.writeAnalysis(twitter_model_100, 'glove-wiki-gigaword-100')
analyzer.writeAnalysis(twitter_model_100, 'glove-wiki-gigaword-50')
analyzer.writeAnalysis(twitter_model_100, 'gglove-wiki-gigaword-200')

