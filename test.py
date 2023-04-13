import nltk
import pymorphy2

grammar = r"""
        PP: {<PREP><NP|CC>}
        NP: {<PRCL>?<ADJF>*<NUMR>*<NOUN|NPRO><ADJF>*<NOUN>*<PP>*}
        CC: {<VP|NP|ADVP|CC|ADJF><CONJ><VP|NP|ADVP|CC|ADJF>}
        PP: {<PREP><NP|CC>}
        ADVP: {<ADVB><PP>}
              {<ADVB>+<NP>}
              {<ADVB>*}
              
        CC: {<VP|NP|ADVP|CC|ADJF><CONJ><VP|NP|ADVP|CC|ADJF>}
        VP: {<PRCL>?<ADVP>*<VERB|INFN><INFN|VERB>*<NP>*<ADVP>*<CC>*<PP>*}
            {<PRCL>?<PP>*<VERB>}
        CC: {<VP|NP|ADVP|CC|ADJF><CONJ><VP|NP|ADVP|CC|ADJF>}
        
"""

def read_file():
    with open('filename.txt', 'r') as file:

        data = file.read()
        return data


def write_file(data):
    with open('my_file.txt', 'w') as f:
        f.write(data)


# =================================
text = 'Моя мама моет и красит белую раму дважды в месяц. ' \
           'А я сижу рядом с ней и ем яблоки и сладкие груши. ' \
           'Сегодня вечером я собираюсь приготовить пасту с жареными креветками и чесноком. ' \
           'Мой папа уже двадцать лет работает главным анестезиологом в городской клинической больнице. ' \
           'Он работал там еще тогда, когда я не родилась. '
def decompose(text):
    morph = pymorphy2.MorphAnalyzer()
    sentences = nltk.sent_tokenize(text)
    res_string = "(TEXT "
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        print(tokens)
        tagged_words = [(w, morph.parse(w)[0].tag.POS) for w in tokens if morph.parse(w)[0].tag.POS is not None]
        print(tagged_words)
        cp = nltk.RegexpParser(grammar)
        buffer_res = cp.parse(tagged_words)
        res_string = res_string + str(buffer_res) + "\n"
    res_string += ")"
    result = nltk.Tree.fromstring(res_string)
    return res_string, result

