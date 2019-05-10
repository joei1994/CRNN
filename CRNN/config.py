# Constants

# Supported characters
CHAR_VECTOR = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'.!?,\"")

thai_alphabets = [chr(i) for i in range(ord('ก'), ord('ฮ'))]
thai_vowels = [chr(i) for i in range(ord('ะ'), ord('์'))]

CHAR_VECTOR = CHAR_VECTOR + thai_alphabets + thai_vowels

# Number of classes
NUM_CLASSES = len(CHAR_VECTOR) + 1
