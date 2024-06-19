import string, base64, codecs
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def to_numbers(value):
  new = ""
  letters = list(string.ascii_letters)
  for let in value:
    if let in letters:
      new += str(letters.index(let))
    else:
      new += let
  p = 0
  while len(new) < 16:
    p += 1
    new += oct(p)
  new = base64.b85encode(new.encode()).decode()
  new = new[:16]
  new = codecs.encode(new, 'rot13')

  return new.encode()


def encrypt(string):
  ukey = input("Key: ")
  key = to_numbers(ukey)

  # Make the cipher
  cipher = AES.new(key, AES.MODE_CBC)
  # Encrypt the string
  ciphertext_bytes = cipher.encrypt(pad(string.encode(), AES.block_size))
  # Grab the IV
  init_vector = cipher.iv
  # Grab the string from ciphertext bytes
  ciphertext = ciphertext_bytes
  # Return it
  return key, init_vector, ciphertext


def decrypt(string, initvector, key):
  # Make the cipher
  cipher = AES.new(key, AES.MODE_CBC, initvector)
  # Unpad and decrypt the given string
  passedtext = unpad(cipher.decrypt(string), AES.block_size)
  # Return the decrypted value
  return passedtext


key, initvector, ciphertext = encrypt("Hello World")
print("""
↣ Key   : {}
↣ IV    : {}
↣ CT    : {}
""".format(key, initvector, ciphertext))

decrypt_value = decrypt(ciphertext, initvector, key)
print("↣ Value : {}".format(decrypt_value))
