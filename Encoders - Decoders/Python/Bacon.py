import argparse, string

bacon_cipher = {
    'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011',
    'E': '00100', 'F': '00101', 'G': '00110', 'H': '00111',
    'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011',
    'M': '01100', 'N': '01101', 'O': '01110', 'P': '01111',
    'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011',
    'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111',
    'Y': '11000', 'Z': '11001'
}
#𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭
typeface_2 = {
    "A" : "𝗔",
    "B" : "𝗕",
    "C" : "𝗖",
    "D" : "𝗗",
    "E" : "𝗘",
    "F" : "𝗙",
    "G" : "𝗚",
    "H" : "𝗛",
    "I" : "𝗜",
    "J" : "𝗝",
    "K" : "𝗞",
    "L" : "𝗟",
    "M" : "𝗠",
    "N" : "𝗡",
    "O" : "𝗢",
    "P" : "𝗣",
    "Q" : "𝗤",
    "R" : "𝗥",
    "S" : "𝗦",
    "T" : "𝗧",
    "U" : "𝗨",
    "V" : "𝗩",
    "W" : "𝗪",
    "X" : "𝗫",
    "Y" : "𝗬",
    "Z" : "𝗭",
    " " : "-"
}

cipher_text = """Cryptographyorcryptologyisthepracticeandstudyoftechniquesforsecurecommunicationinthepresenceofadversarialbehavior.2Moregenerallycryptographyisaboutconstructingandanalyzingprotocolsthatpreventthirdpartiesorthepublicfromreadingprivatemessages.3Moderncryptographyexistsattheintersectionofthedisciplinesofmathematicscomputerscienceinformationsecurityelectricalengineeringdigitalsignalprocessingphysicsandothers.4Coreconceptsrelatedtoinformationsecurity(dataconfidentialitydataintegrityauthenticationandnon-repudiation)arealsocentraltocryptography.5Practicalapplicationsofcryptographyincludeelectroniccommercechip-basedpaymentcardsdigitalcurrenciescomputerpasswordsandmilitarycommunications."""


def encode(word):
    cypher = ""
    bacons = []
    for a in word:
        if a == " ":
            bacons.append("-")
        else:
            bacons.append(bacon_cipher[a.upper()])


    for i, bacon in enumerate(bacons):
        start_index = i * 5
        x = ""
        chunk = cipher_text[start_index:start_index + 5]

        for j in range(5):
            if bacon[j] == "-":
                x += "-"
                break
            elif bacon[j] == "1":
                x += typeface_2.get(chunk[j].upper())
            else:
                x += chunk[j]
        cypher += x
    print(cypher + cipher_text[len(cypher):])

def decode(word):
    chunks = [word[i:i+5] for i in range(0, len(word), 5)]
    vals = []
    new_dic = {value: key for key, value in bacon_cipher.items()}
    og = ""
    for chunk in chunks:
        x = ""
        for a in chunk:
            a = a.upper()
            if a not in bacon_cipher.keys():
                x += "1"
            else:
                x += "0"
        vals.append(x)
    for val in vals:
        og += new_dic.get(val, " ")
    print(og)        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bacon encoder and decoder")
    parser.add_argument("--mode", "-m", help="encode or decode")
    parser.add_argument("--string", "-s", help="String")

    args = parser.parse_args()

    if args.mode == "encode":
       encode(args.string)
    elif args.mode == "decode":
        decode(args.string)
    else:
        print("Please specify a mode")