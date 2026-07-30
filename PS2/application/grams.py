# Abraham Sharum
# CS4343
# PS2
# Due Date: September 30, 2024 11:00PM
import math
import json
import os
def tokenize_doc_unis(doc):
    unigram_lm = dict()
    for token in doc:
        if token in unigram_lm:
            unigram_lm[token] += 1
        else:
            unigram_lm[token] = 1
        
    return unigram_lm   

def tokenize_doc_bis(doc,unigram_lm):
    bigram_lm = dict()

    for i in range(0, len(doc) - 1,):
        bigram = doc[i] + " " + doc[i+1]

        if bigram in bigram_lm:
            bigram_lm[bigram] += 1
        else:
            bigram_lm[bigram] = 1

    uni = len(unigram_lm)
    
    for key in bigram_lm.keys():
        temp = key.split()
        bigram_lm[key] = math.log((bigram_lm[key] + 1)) - math.log((unigram_lm[temp[0]] + uni))

    return bigram_lm   

def tokenize_doc_tri(doc):
    trigram_lm = dict()

    for i in range(0, len(doc) - 2,):
        trigram = doc[i] + " " + doc[i+1] + " " + doc[i+2]

        if trigram in trigram_lm:
            trigram_lm[trigram] += 1
        else:
            trigram_lm[trigram] = 1

        
    return trigram_lm   

def nested(n_gram):
    nested_ngrams = dict()

    
    for key, freq in n_gram.items():
        key = key.split()
        if len(key) > 2:
            if key[0] not in nested_ngrams:
                nested_ngrams[key[0]] = dict()
        
            if key[1] not in nested_ngrams[key[0]]:
                nested_ngrams[key[0]][key[1]] = dict()
                
            nested_ngrams[key[0]][key[1]][key[2]] = freq

        elif len(key) > 1:
            if key[0] not in nested_ngrams:
                nested_ngrams[key[0]] = dict()
        
            nested_ngrams[key[0]][key[1]] = freq

    return nested_ngrams

def find_input_prob(sentence,unigrams):

    probs = dict()
    sentence = sentence.split()

    for word in sentence:
        try:
            probs[word] = math.log(unigrams[word]) - math.log(sum(unigrams.values()))
        except:
            print(f"{word} is not in the training data!")
            probs[word] = 0 
    return probs

def save_to_file(to_save,file_name,is_output):
    if is_output:
        parent_dir = "./output/"
    else:
        parent_dir = "./ngrams/"

    try:
        os.makedirs("./ngrams")
    except:
        pass
    try:
        os.makedirs("./output")
    except:
        pass
    
    
    if is_output:
        with open(parent_dir + file_name + ".json", "w") as file:
            json.dump(to_save, file,indent=2)
    else:
        with open(parent_dir + file_name + ".json", "w") as file:
            json.dump(to_save, file)