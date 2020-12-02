import numpy as np
from simple_perceptron import SimplePerceptron


SYMBOL_TO_FLOAT = {
    '-': 1,
    '.': -1,
    '0': 0,
    ' ': 0,
}


LETTER_TO_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    ' ': ' '
}


CODE_TO_FLOATS = {}

for letter, code_value in LETTER_TO_CODE.items():
    floats = [SYMBOL_TO_FLOAT[symbol] for symbol in code_value.zfill(6)]
    floats = tuple(floats)
    CODE_TO_FLOATS[letter] = floats

FLOATS_TO_CODE = dict(zip(CODE_TO_FLOATS.values(), CODE_TO_FLOATS.keys()))


LETTER_TO_FLOATS = {}

for i, letter in enumerate(LETTER_TO_CODE.keys()):
    floats = [0] * len(LETTER_TO_CODE)
    floats[i] = 1
    floats = tuple(floats)
    LETTER_TO_FLOATS[letter] = floats

FLOATS_TO_LETTER = dict(zip(CODE_TO_FLOATS.values(), CODE_TO_FLOATS.keys()))


encode_inputs = np.array(list([list(floats) for floats in LETTER_TO_FLOATS.values()]))
encode_outputs = np.array(list([list(floats) for floats in CODE_TO_FLOATS.values()]))


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class MorseEncodePerceptron(SimplePerceptron):
    def __init__(self):
        super(MorseEncodePerceptron, self).__init__(None, 44, 6)

    def encode_letter(self, letter_floats):
        return tuple(self.execute(letter_floats, rounded=False))

    def encode(self, phrase):
        cipher = ''

        for letter in phrase.upper():
            letter_floats = list(LETTER_TO_FLOATS[letter])
            code_floats = tuple(self.execute(letter_floats, rounded=True))
            code_string = FLOATS_TO_CODE[code_floats]
            cipher += code_string.strip('0')

        return cipher

