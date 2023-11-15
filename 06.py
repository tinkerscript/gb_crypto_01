import sys
from decoder import decode


def main():
    target_file = open('6.txt', 'r')
    lines = target_file.readlines()
    best = {
        'score': sys.maxsize,
        'value': None
    }

    variants_list = []

    for line in lines:
        variant = decode(bytes.fromhex(line))
        variants_list.append(variant)
        if variant['score'] < best['score']:
            best = variant

    for a in sorted(variants_list, key=lambda x: x['score'], reverse=True):
        print(a)

    print(f'Вариант: "{best["value"].decode()}", расхождение {best["score"]}')


if __name__ == '__main__':
    main()
