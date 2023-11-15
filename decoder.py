import sys

LETTERS_FREQUENCY = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881,
    'g': 0.0158610, 'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490,
    'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563,
    's': 0.0515760, 't': 0.0729357, 'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692,
    'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


def single_byte_xor(encoded, key):
    encoded_byte_array = bytearray(len(encoded))
    for i in range(len(encoded_byte_array)):
        encoded_byte_array[i] = encoded[i] ^ key
    return encoded_byte_array


def group_characters(encoded):
    groups = {}

    for byte in encoded:
        if not groups.get(byte):
            groups[byte] = 0

        groups[byte] += 1

    return groups


def get_score(encoded):
    groups = group_characters(encoded)
    score = 0

    for byte in groups:
        ideal_frequency = LETTERS_FREQUENCY.get(chr(byte), 0)
        current_frequency = groups[byte] / len(encoded)
        score += abs(current_frequency - ideal_frequency) if ideal_frequency else 1

    return score


def decode(encoded_bytes):
    best = {
        'score': sys.maxsize,
        'value': None
    }

    for key in range(256):
        encoded = single_byte_xor(encoded_bytes, key)
        score = get_score(encoded)

        if score < best['score']:
            best['score'] = score
            best['value'] = encoded

    return best


def main():
    hexed = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    best = decode(bytes.fromhex(hexed))
    print(f'Вариант: "{best["value"].decode()}", расхождение {best["score"]}')


if __name__ == '__main__':
    main()
