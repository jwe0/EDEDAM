import argparse

square = """
ABCDE
FGHJK
LMNOP
QRSTU
VWXYZ
"""

def encode(word):
    result = ""
    rows = [square for square in square.split("\n") if square != ""]
    col_in = 0
    row_in = 0
    for char in word.upper():
        if char == " ":
            result += ""
        for row in rows:
            if char in row:
                row_in = rows.index(row) + 1
                col_in = row.index(char) + 1
                result += "{}{}".format(str(row_in), str(col_in))
                continue
    print(result)

def decode(word):
    result = ""
    rows = [square for square in square.split("\n") if square != ""]
    for i in range(0, len(word), 2):
        row_in = int(word[i]) - 1  
        col_in = int(word[i+1]) - 1 
        result += rows[row_in][col_in]
    print(result)
                    
                        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Polybius encoder/decoder")

    parser.add_argument("--mode", help="encode / decode")
    parser.add_argument("--string", help="String to encode / decode")

    args = parser.parse_args()

    if args.mode == "encode":
        encode(args.string)
    elif args.mode == "decode":
        decode(args.string)
    else:
        print("Run with --help for help")