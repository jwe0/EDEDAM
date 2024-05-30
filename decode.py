import sys


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




base64decode(sys.argv[1])
