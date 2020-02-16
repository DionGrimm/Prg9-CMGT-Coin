import requests
from mod10sha import hash
from hashlib import sha256
import json
import sys
import schedule
import time
import secrets

sys.setrecursionlimit(150000)

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
    time.sleep(1)
    # Try to create a valid hash with different nonce values
    def findValidNonce(count = 0):
        count += 1
        if count > 500: return mine()
        nonce = secrets.randbelow(999999)
        stringToHash = f'{hashedBlock}{transactions[0]["from"]}{transactions[0]["to"]}{transactions[0]["amount"]}{transactions[0]["timestamp"]}{timestamp}{nonce}'
        hashToCheck = encrypt_string(hash(stringToHash))
        print(hashToCheck)
        if hashToCheck.startswith('0000'): return nonce
        return findValidNonce(count)

    validNonce = findValidNonce()
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