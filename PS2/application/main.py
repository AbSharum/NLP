# Abraham Sharum
# CS4343
# PS2
# Due Date: September 30, 2024 11:00PM
import string
import grams
import json
import time

doc = open("./shakespear.txt","r")
doc = doc.read()
doc = doc.translate(str.maketrans('', '',string.punctuation))
doc = doc.lower()
doc = doc.split()

to_save = input(str("Would you to load or save the dictonaries? 'l\\s': "))

if to_save.lower() == 's':
    to_save = True
elif to_save.lower() == 'l':
    to_save = False

if (to_save == True):
    print("saving...")
    unigram_lm = grams.tokenize_doc_unis(doc)
    bigram_lm = grams.tokenize_doc_bis(doc,unigram_lm)
    trigram_lm = grams.tokenize_doc_tri(doc)

    nested_bigrams = grams.nested(bigram_lm)
    nested_trigrams = grams.nested(trigram_lm)
    
    grams.save_to_file( unigram_lm, "unigrams",False)
    grams.save_to_file( bigram_lm, "bigrams",False)
    grams.save_to_file( trigram_lm, "trigrams",False)
    grams.save_to_file( nested_bigrams, "nbigrams",False)
    grams.save_to_file( nested_trigrams, "ntrigrams",False)
    print("Save complete!")

else:
    print("loading....")
    unigram_lm = json.loads(open("./ngrams/unigrams.json").read())
    bigram_lm = json.loads(open("./ngrams/bigrams.json").read())
    trigram_lm = json.loads(open("./ngrams/trigrams.json").read())
    nested_bigrams = json.loads(open("./ngrams/nbigrams.json").read())
    nested_trigrams = json.loads(open("./ngrams/ntrigrams.json").read())
    print("All dictonaries loaded!")

def main(message,n_gram):
 
    #predict the output

    def predict_next(input):
        for i in range(10):
            try:
                if i == 0:
                    input += " " + predict(input.split()) + " "
                elif i < 9:
                    input += predict(input.split()) + " "
                else:
                    input += predict(input.split())
            except:
                return input.split()[len(input.split())-1],0

        probs = grams.find_input_prob(input,unigram_lm)
        return input, probs
    
    def predict(words):
        if len(words) >= 2:
            first_word = words[len(words)-2]
        if len(words) >= 1:
            second_word = words[len(words)-1]
            

        if(len(words) >= 2 and n_gram == "tri"):


            if first_word in nested_trigrams and second_word in nested_trigrams[first_word]:
                next_word = getWord(nested_trigrams[first_word][second_word])
            if next_word == None and second_word in nested_bigrams:
                next_word = getWord(nested_bigrams[second_word])
            return next_word
        
        
        elif(len(words) >= 1):
            if second_word in nested_bigrams:
                next_word = getWord(nested_bigrams[second_word])
                return next_word
            
    def getWord(possible_next):
            #code using max.choices() for weighted probabilities
            num_items = len(possible_next.items())
            word_probs = [None] * num_items
            i = 0
            total = sum(possible_next.values())

            for count in possible_next.values():
                word_probs[i] = count / total
                if i < num_items:
                    i+=1

            choice = max(random.choices(list(possible_next.keys()),word_probs))
            #choice = max(possible_next, key=possible_next.get)
            
            return choice

    return predict_next(message)