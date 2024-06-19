import argparse, sys

def base64encode(s):
    base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base64 = ''

    padding = (3 - len(s) % 3) % 3
    s += '\0' * padding

    for i in range(0, len(s), 3):
        byte1 = ord(s[i])
        byte2 = ord(s[i + 1])
        byte3 = ord(s[i + 2])

        binary1 = f'{byte1:08b}'
        binary2 = f'{byte2:08b}'
        binary3 = f'{byte3:08b}'

        combined = binary1 + binary2 + binary3

        base64 += base64chars[int(combined[0:6], 2)]
        base64 += base64chars[int(combined[6:12], 2)]
        base64 += base64chars[int(combined[12:18], 2)]
        base64 += base64chars[int(combined[18:24], 2)]

    if padding:
        base64 = base64[:-padding] + "=" * padding

    print(base64)

def base64decode(s):
    base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    decoded = ''

    padding_length = s.count("=")
    s = s.rstrip("=") + "A" * padding_length

    for i in range(0, len(s), 4):
        num = 0

        for j in range(4):
            num += base64chars.index(s[i + j]) * (64 ** (3 - j))
     
     
        byte1 = num // (256 ** 2)
        byte2 = (num % (256 ** 2)) // 256
        byte3 = num % 256

        decoded += chr(byte1)
        decoded += chr(byte2)
        decoded += chr(byte3)

    if padding_length:
        decoded = decoded[:-padding_length]
    print(decoded)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Base64 encoder and decoder")
    parser.add_argument("--mode", "-m", help="encode or decode")
    parser.add_argument("--input", "-i", help="String")

    args = parser.parse_args()

    if args.mode == "encode":
        base64encode(args.input)
    elif args.mode == "decode":
        base64decode(args.input)
    else:
        print("Please specify a mode")

