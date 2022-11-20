import spacy
from flask import jsonify
from collections import Counter
from string import punctuation
import pandas as pd

#python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

class NLP_Model(object):

    # Find named entities, phrases and concepts
    def get_entities(self, senttext):
        # Process whole documents

        doc = nlp(senttext)  # process the text sent from android

        dictionary_of_entities = []
        count = 0
        for entity in doc.ents:
            dic1 = {}  # here we define an empty dictionary
            dic1['text'] = entity.text
            dic1['label'] = entity.label_
            dictionary_of_entities.append(dic1)
            count += 1
        set_of_distinct_dictionaries_of_entities=pd.DataFrame(dictionary_of_entities).drop_duplicates().to_dict('records')#remove duplicate dictionaries



        return jsonify(set_of_distinct_dictionaries_of_entities)

    def get_hotwords(self, text): # https://medium.com/better-programming/extract-keywords-using-spacy-in-python-4a8415478fbf
        result = []
        pos_tag = ['PROPN', 'ADJ', 'NOUN']  # 1
        doc = nlp(text.lower())  # 2
        for token in doc:
            # 3
            if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
                continue
            # 4
            if (token.pos_ in pos_tag):
                result.append(token.text)

        return result  # 5

    # def summarize_advanced(self,text,limit):
    #     nlp = pipeline('summarization')
    #     return  nlp(text)

    def top_sentence(self, text, limit):#summarize in an extractive way
        keyword = []
        pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
        doc = nlp(text.lower())
        for token in doc:
            if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
                continue
            if (token.pos_ in pos_tag):
                keyword.append(token.text)

        freq_word = Counter(keyword)
        max_freq = Counter(keyword).most_common(1)[0][1]
        for w in freq_word:
            freq_word[w] = (freq_word[w] / max_freq)

        sent_strength = {}
        for sent in doc.sents:
            for word in sent:
                if word.text in freq_word.keys():
                    if sent in sent_strength.keys():
                        sent_strength[sent] += freq_word[word.text]
                    else:
                        sent_strength[sent] = freq_word[word.text]

        summary = []

        sorted_x = sorted(sent_strength.items(), key=lambda kv: kv[1], reverse=True)

        counter = 0
        for i in range(len(sorted_x)):
            summary.append(str(sorted_x[i][0]).capitalize())

            counter += 1
            if counter >= int(limit):
                break

        return ' '.join(summary)
