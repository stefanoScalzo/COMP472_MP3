# %%
import pandas as pd
import csv
from gensim.models.word2vec import Word2Vec
from gensim.models import KeyedVectors
df = pd.read_csv("synonyms.csv")
model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)

# %%
f = open('./KeyedVectors-details.csv', 'w')
writer = csv.writer(f)
for array in df.values:
    highestScore = 0
    d = ""
    type = "guess"
    for (index,word) in enumerate (array):
        if(word in model.key_to_index and array[0] in model.key_to_index):
            if(index > 1 and model.distance(array[0], word) > highestScore):
                highestScoreWord = word
            
    if(array[0] not in model.key_to_index or len(list(filter(lambda x: x in model.key_to_index, array)))<2):
        type = "guess"
    elif(array[1]==highestScoreWord):
        type = "correct"
    else: 
        type = "wrong"

    writer.writerow([array[0],array[1],highestScoreWord,type])
f.close()



