from binascii import hexlify


def repeating_key_xor(target, key):
    key_string = (key * len(target))[0:len(target)]
    encoded_byte_array = bytearray(len(target))

    for i in range(len(target)):
        encoded_byte_array[i] = target[i] ^ key_string[i]

    return encoded_byte_array


def main():
    first = b"Bohemian Rhapsody"
    second = b'I go crazy when I hear a cymbal'
    key = b'Queen'

    print(hexlify(repeating_key_xor(first, key)))
    print(hexlify(repeating_key_xor(second, key)))


if __name__ == '__main__':
    main()
