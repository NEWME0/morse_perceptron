from .morse_dictionary import MorseDictionary
from .morse_perceptron import MorsePerceptron


if __name__ == '__main__':
    phrase = "Hello motherfucker"
    print('Initial phrase and alignment: ', phrase, '\n')

    morse_dictionary_cipher = MorseDictionary.encode(phrase)
    print('Encoded with MorseDictionary: ', morse_dictionary_cipher)
    morse_perceptron_cipher = MorsePerceptron.encode(phrase)
    print('Encoded with MorsePerceptron: ', morse_perceptron_cipher)

    print('')

    morse_dictionary_result = MorseDictionary.decode(morse_dictionary_cipher)
    print('Decoded with MorseDictionary: ', morse_dictionary_result)
    morse_perceptron_cipher = MorsePerceptron.decode(morse_perceptron_cipher)
    print('Decoded with MorsePerceptron: ', morse_perceptron_cipher)
