from binascii import hexlify


def repeating_key_xor(string, key):
    key_string = (key * len(string))[0:len(string)]
    encoded_byte_array = bytearray(len(string))

    for i in range(len(string)):
        encoded_byte_array[i] = ord(string[i]) ^ ord(key[i])

    return encoded_byte_array


def main():
    first = "Burning 'em, if you ain't quick and nimble"
    second = "Bohemian Rhapsody"
    key = 'Queen'

    print(hexlify(repeating_key_xor(first, key)))
    print(hexlify(repeating_key_xor(second, key)))


if __name__ == '__main__':
    main()
