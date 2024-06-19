import string, argparse



def encode(word, shift):
    new = []

    for char in word:
        if char in string.ascii_lowercase:
            new.append(string.ascii_lowercase[(string.ascii_lowercase.index(char) + shift) % len(string.ascii_lowercase)])
        else:
            new.append(char)
            
    print("".join(new))

def decode(word, shift):
    new = []
    for char in word:
        if char in string.ascii_lowercase:
            new.append(string.ascii_lowercase[(string.ascii_lowercase.index(char) - shift) % len(string.ascii_lowercase)])
        else:
            new.append(char)

    print("".join(new))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rot encoder/decoder")

    parser.add_argument("--mode", help="encode / decode")
    parser.add_argument("--string", help="String to encode / decode")
    parser.add_argument("--shift", help="Shift by value")

    args = parser.parse_args()

    if args.mode == "encode":
        encode(args.string.lower(), int(args.shift))
    elif args.mode == "decode":
        decode(args.string.lower(), int(args.shift))
    else:
        print("Run with --help for help")
