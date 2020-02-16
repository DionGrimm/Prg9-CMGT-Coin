import requests
from mod10sha import hash
from hashlib import sha256
import json
import sys
import schedule
import time
import secrets

sys.setrecursionlimit(20000)

def encrypt_string(hashString):
    sha_signature = \
        sha256(hashString.encode()).hexdigest()
    return sha_signature

url = 'https://programmeren9.cmgt.hr.nl:8000/api/blockchain/next'

def mine():
    jsonData = json.dumps(requests.get(url).json())
    blockchain = json.loads(jsonData)['blockchain']
    transactions = json.loads(jsonData)['transactions']
    timestamp = json.loads(jsonData)['timestamp']

    # Hash string from previous block
    stringFromPreviousBlock = f'{blockchain["hash"]}{blockchain["data"][0]["from"]}{blockchain["data"][0]["to"]}{blockchain["data"][0]["amount"]}{blockchain["data"][0]["timestamp"]}{blockchain["data"][0]["timestamp"]}{blockchain["nonce"]}'

    hashedBlock = encrypt_string(hash(stringFromPreviousBlock))

    # Try to create a valid hash with different nonce values
    def findValidNonce(nonce, nonceTry = 0):
        nonceTry = nonce + 1
        if nonceTry > nonce + 1000: return mine()
        stringToHash = f'{hashedBlock}{transactions[0]["from"]}{transactions[0]["to"]}{transactions[0]["amount"]}{transactions[0]["timestamp"]}{timestamp}{nonceTry}'
        hashToCheck = encrypt_string(hash(stringToHash))
        print(hashToCheck)
        if hashToCheck.startswith('0000'): return nonceTry
        return findValidNonce(nonce, nonceTry)

    validNonce = findValidNonce(secrets.randbelow(9999))
    print(validNonce)
    # Post the valid nonce
    urlForPost = 'https://programmeren9.cmgt.hr.nl:8000/api/blockchain'
    data = {
        'nonce': validNonce,
        'user': 'Dion 0906233'
    }

    requests.post(urlForPost, json.dumps(data))

mine()
# schedule.every(1).minutes.do(mine)

# while 1:
#     schedule.run_pending()
#     time.sleep(1)