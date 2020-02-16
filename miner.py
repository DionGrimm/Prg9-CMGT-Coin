import requests
from mod10sha import hash
from hashlib import sha256
import json
import sys
import schedule
import time
import secrets

sys.setrecursionlimit(999999)

def encrypt_string(hashString):
    sha_signature = \
        sha256(hashString.encode()).hexdigest()
    return sha_signature

url = 'https://programmeren9.cmgt.hr.nl:8000/api/blockchain/next'
jsonData = json.dumps(requests.get(url).json())
blockchain = json.loads(jsonData)['blockchain']
transactions = json.loads(jsonData)['transactions']
timestamp = json.loads(jsonData)['timestamp']

# Hash string from previous block
stringFromPreviousBlock = f'{blockchain["hash"]}{blockchain["data"][0]["from"]}{blockchain["data"][0]["to"]}{blockchain["data"][0]["amount"]}{blockchain["data"][0]["timestamp"]}{blockchain["timestamp"]}{blockchain["nonce"]}'

hashedBlock = encrypt_string(hash(stringFromPreviousBlock))
# Try to create a valid hash with different nonce values
def findValidNonce():
    for i in range(999999):
        nonce = i + secrets.randbelow(99999)
        stringToHash = f'{hashedBlock}{transactions[0]["from"]}{transactions[0]["to"]}{transactions[0]["amount"]}{transactions[0]["timestamp"]}{timestamp}{nonce}'
        hashToCheck = encrypt_string(hash(stringToHash))
        print(i, nonce, hashToCheck)
        if hashToCheck.startswith('0000'):
            return str(nonce)

validNonce = findValidNonce()
# Post the valid nonce
url = 'https://programmeren9.cmgt.hr.nl:8000/api/blockchain'
data = {
    'nonce': validNonce,
    'user': 'Dion 0906233'
}

post = requests.post(url, data = data)
print(post.text)
