# %%
from ModelExecutor import ModelExecutor


model_executor = ModelExecutor()
model_executor.runModel('./GoogleNews-vectors-negative300.bin.gz','./KeyedVectors-details.csv')
