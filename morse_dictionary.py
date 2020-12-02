

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
}


CODE_TO_LETTER = dict(zip(LETTER_TO_CODE.values(), LETTER_TO_CODE.keys()))


class MorseDictionary:
    @classmethod
    def encode(cls, phrase):
        cipher = ''

        for letter in phrase.upper():
            code = LETTER_TO_CODE.get(letter)
            cipher += code + ' ' if code else ' '

        return cipher

    @classmethod
    def decode(cls, cipher):
        phrase = ''

        for code in cipher.strip(' ').split(' '):
            letter = CODE_TO_LETTER.get(code)
            phrase += letter if letter else ' '

        return phrase
