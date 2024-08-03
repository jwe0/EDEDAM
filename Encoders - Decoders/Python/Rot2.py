import argparse


def encode(string, shift):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(alph[(alph.index(char) + shift) % 26] if char in alph else char for char in string)

def decode(string, shift):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(alph[(alph.index(char) - shift) % 26] if char in alph else char for char in string)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rot encoder/decoder")

    parser.add_argument("--mode", help="encode / decode")
    parser.add_argument("--string", help="String to encode / decode")
    parser.add_argument("--shift", help="Shift by value")

    args = parser.parse_args()

    if args.mode == "encode":
        print(encode(args.string.lower(), int(args.shift)))
    elif args.mode == "decode":
        print(encode(args.string.lower(), int(args.shift)))
    else:
        print("Run with --help for help")