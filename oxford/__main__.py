import requests

# Oxford Dictionary API


class Oxford:

    def __init__(self, app_id, app_key, language):
        self.app_id = app_id
        self.app_key = app_key
        self.language = language

    def get_word(self, word):
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + \
            self.language + '/' + word.lower()
        headers = {'app_id': self.app_id, 'app_key': self.app_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_word_definitions(self, word):
        word_definitions = []
        word_definitions_json = self.get_word(word)
        for word_definition in word_definitions_json['results'][0]['lexicalEntries'][0]['entries'][0]['senses']:
            word_definitions.append(word_definition['definitions'][0])
        return word_definitions

    def get_word_synonyms(self, word):
        word_synonyms = []
        word_synonyms_json = self.get_word(word)
        for word_synonym in word_synonyms_json['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']:
            word_synonyms.append(word_synonym['text'])
        return word_synonyms

    def get_word_antonyms(self, word):
        word_antonyms = []
        word_antonyms_json = self.get_word(word)
        for word_antonym in word_antonyms_json['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['antonyms']:
            word_antonyms.append(word_antonym['text'])
        return word_antonyms

    def get_word_examples(self, word):
        word_examples = []
        word_examples_json = self.get_word(word)
        for word_example in word_examples_json['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples']:
            word_examples.append(word_example['text'])
        return word_examples
