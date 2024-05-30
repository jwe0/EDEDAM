import sys


def encoder(s):
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




encoder(sys.argv[1])