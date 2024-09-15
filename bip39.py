# This script is designed to create or recreate 
# the key and password used to manage a digital legacy.
#
# To recover the partial passphrase, a minimum of two 
# recovery cards must be combined.
#
# Author: Ulf Schmelzer

from mnemonic import Mnemonic
from hashlib import pbkdf2_hmac
import base64
import sys

mnemo = Mnemonic("english")

if sys.argv[1:]:
    words = " ".join(sys.argv[1:])
else:
    words = mnemo.generate(strength=256)

print("Word list:", words)
bip39seed = mnemo.to_seed(words, passphrase="")

print("BIP39 seed (hex):", bip39seed.hex())
print("BIP39 seed (base64):", base64.b64encode(bip39seed).decode('utf-8'))
pw = pbkdf2_hmac('sha512', bip39seed, b'myDigitalLegacy' * 2, 100_000)
print("Password:", base64.b64encode(pw).decode('utf-8')[:12])

lst = words.split()

card1 = [lst[0], 'XXXX', lst[2], 'XXXX', 'XXXX', lst[5], 'XXXX', lst[7], lst[8], 'XXXX', lst[10], lst[11], lst[12], lst[13],  'XXXX', lst[15], lst[16],  'XXXX', lst[18], lst[19], lst[20],  'XXXX', lst[22], lst[23]]
card2 = [lst[0], lst[1], 'XXXX', lst[3], lst[4], 'XXXX', lst[6], lst[7], 'XXXX', lst[9], lst[10],  'XXXX', lst[12],  'XXXX', lst[14],  'XXXX', lst[16], lst[17], lst[18],  'XXXX', lst[20], lst[21],  'XXXX', lst[23]]
card3 = ['XXXX', lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], 'XXXX', lst[8], lst[9],  'XXXX', lst[11],  'XXXX', lst[13], lst[14], lst[15],  'XXXX', lst[17],  'XXXX', lst[19],  'XXXX', lst[21], lst[22],  'XXXX']

print("Card 1:", " ".join(card1))
print("Card 2:", " ".join(card2))
print("Card 3:", " ".join(card3))
