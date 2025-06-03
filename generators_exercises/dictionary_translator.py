def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    trans_sentence = (words[w] for w in sentence.split(" "))
    return ' '.join([word for word in trans_sentence])


print(translate("el gato esta en la casa"))
