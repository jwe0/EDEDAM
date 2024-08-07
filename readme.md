# Encoders, Decoders, Encryptors, Decryptors and More
Contains some snippets of code for different algorithms relating to the different sectors of Cryptography.


## Encoders

### Base64
Encode text with the Ascii Table
```
python3 Base64.py --mode encode --input Test
```

### Rot
Also known as Caesar cipher named after Julius Caesar. Rot shifts the letter to a different letter based on a shift value like 13. For example in rot13 a becomes n.
```
python3 Rot.py --mode encode --string Test --shift 13
```

### Rot 2
A more clean version of the original Rot encoder.
```
python3 Rot.py --mode encode --string Test --shift 13
```

### Bacon
A classical cypher known as Bacon or Baconian cypher named after Francis Bacon that utilizes 2 different type faces to hide your message.
```
python3 Bacon.py -m encode -s "Hello"
```


## Sorting Algorithms

### Selection
Selection sort iterates through a list and checks if the number is larger than the previous number and if it is then it appends to a new array and removes that number from the original array. Selection sort continues until the list is completly sorted
```
# Open the file and input an array
```

### Selection V2
Uses the same sort of idea as the original Selection sort algorithm except uses max() and min() instead of a 
custom sycle that may slow down the sorting
```
# Open the file and input an array
```

## Encryptors

### AES CBC
An implementation of AES encryption with the pycrytodome library. Contains a custom function to generate more random keys from your password by encoding in base85 and using rot13 to also ensure it is 16 chars long.
```
python3 "Aes CBC.py"
```
