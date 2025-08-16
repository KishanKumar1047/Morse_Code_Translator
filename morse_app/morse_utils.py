import difflib

# Morse dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

# Reverse dictionary for Morse → English
MORSE_TO_ENG = {v: k for k, v in MORSE_CODE_DICT.items()}

# English → Morse
def text_to_morse(text):
    text = text.upper()
    return ' '.join(MORSE_CODE_DICT.get(char, '') for char in text if char != ' ')

# Morse → English
def morse_to_text(morse):
    words = morse.split("   ")
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_word = ''.join(MORSE_TO_ENG.get(l, '?') for l in letters)
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)

# Suggest similar words
def suggest_words(word, dictionary):
    return difflib.get_close_matches(word, dictionary, n=5, cutoff=0.6)
