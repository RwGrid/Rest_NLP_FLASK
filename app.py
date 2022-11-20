from flask import Flask, request, jsonify, json
from flask_cors import CORS
from flask_restful import Resource, Api

from collections import Counter
from string import punctuation

import Scrap_Web


from NLP_Models import NLP_Model

app = Flask(__name__)
cors = CORS(app)


nlp_models = NLP_Model()



@app.route('/')
def hello_world():
    #  get request
    return jsonify([{"name": "Rida!"}, {"name": "ahmad"}])


# @app.route('/suma')
# def summarize_advanced():
#     nlp = pipeline('summarization')
#     return nlp("""Bees are flying insects closely related to wasps and ants, known for their role in pollination and, in the case of the best-known bee species, the western honey bee, for producing honey. Bees are a monophyletic lineage within the superfamily Apoidea. They are presently considered a clade, called Anthophila. There are over 16,000 known species of bees in seven recognized biological families.[1][2] Some species — including honey bees, bumblebees, and stingless bees — live socially in colonies while some species — including mason bees, carpenter bees, leafcutter bees, and sweat bees — are solitary.
#
# Bees are found on every continent except for Antarctica, in every habitat on the planet that contains insect-pollinated flowering plants. The most common bees in the Northern Hemisphere are the Halictidae, or sweat bees, but they are small and often mistaken for wasps or flies. Bees range in size from tiny stingless bee species, whose workers are less than 2 millimetres (0.08 in) long, to Megachile pluto, the largest species of leafcutter bee, whose females can attain a length of 39 millimetres (1.54 in).
#
# Bees feed on nectar and pollen, the former primarily as an energy source and the latter primarily for protein and other nutrients. Most pollen is used as food for their larvae. Vertebrate predators of bees include birds such as bee-eaters; insect predators include beewolves and dragonflies.
#
# Bee pollination is important both ecologically and commercially, and the decline in wild bees has increased the value of pollination by commercially managed hives of honey bees. The analysis of 353 wild bee and hoverfly species across Britain from 1980 to 2013 found the insects have been lost from a quarter of the places they inhabited in 1980.[3]
#
# Human beekeeping or apiculture has been practised for millennia, since at least the times of Ancient Egypt and Ancient Greece. Bees have appeared in mythology and folklore, through all phases of art and literature from ancient times to the present day, although primarily focused in the Northern Hemisphere where beekeeping is far more common.""")[
#         0]


@app.route('/keywords', methods=['GET', 'POST'])
def extract_keywords():
    if request.method == 'POST':
        sent_text = request.form.get('text_sent')

        output = set(nlp_models.get_hotwords(sent_text))
        hash_tags = [('#' + x[0]) for x in Counter(output).most_common(5)]

        return jsonify([{"text": ' '.join(hash_tags)}])

    else:
        output = []

        # list_of_entities = json.dumps(dictionary_of_entities, indent=4, sort_keys=True)
        # return jsonify(dictionary_of_entities)
        return jsonify([{"Get request": "BOBO"}, {"Get Request ": "Bobo"}])
 

@app.route('/scrap_text', methods=['GET', 'POST'])
def scrap_url():
    if request.method == 'POST':
        sent_url = request.form.get('url_sent')

       # sent_url='https://www.sciencealert.com/study-finds-just-the-kind-of-people-who-were-panic-buying-all-of-the-toilet-paper'
        article=Scrap_Web.ScrapData().getdata(sent_url)
        return jsonify(
            [{"article_title": article.title, "article_text": article.text}])
    else:
        output = []

        # list_of_entities = json.dumps(dictionary_of_entities, indent=4, sort_keys=True)
        # return jsonify(dictionary_of_entities)
        return jsonify([{"Get request": "BOBO"}, {"Get Request ": "Bobo"}])


@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        sent_text = request.form.get('text_sent')
        size_of_summary = request.form.get('number_of_returned_sentences')
        return jsonify([{"text": nlp_models.top_sentence(sent_text, size_of_summary)}])
    else:
        output = []

        # list_of_entities = json.dumps(dictionary_of_entities, indent=4, sort_keys=True)
        # return jsonify(dictionary_of_entities)
        return jsonify([{"Get request": "BOBO"}, {"Get Request ": "Bobo"}])


@app.route('/entitize', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sent_text = request.form.get('text_sent')
        entities_extracted = nlp_models.get_entities(sent_text)
        # some_json = request.get_data()
        # get data sent
        #  to the url then return it to the sender
        return entities_extracted
    else:
        output = []

        # list_of_entities = json.dumps(dictionary_of_entities, indent=4, sort_keys=True)
        # return jsonify(dictionary_of_entities)
        return jsonify([{"name": "miko"}, {"name": "layla"}])


# if u do not specify the method of rest, it will be
#  automatically be GET 200
@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num * 10})


if __name__ == '__main__':
    app.run(host='192.168.10.134', port=5000)

    #  in debug mode, anytime save it , it will run again
