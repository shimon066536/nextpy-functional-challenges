"""
dictionary_translator.py

Translates a Spanish sentence to English using a predefined dictionary.
"""

def translate(sentence):
    words = {
        'esta': 'is',
        'la': 'the',
        'en': 'in',
        'gato': 'cat',
        'casa': 'house',
        'el': 'the'
    }
    trans_sentence = (words[w] for w in sentence.split(" "))
    return ' '.join(trans_sentence)

def main():
    sentence = "el gato esta en la casa"
    translation = translate(sentence)
    print(f"Original: {sentence}")
    print(f"Translation: {translation}")

if __name__ == "__main__":
    main()
