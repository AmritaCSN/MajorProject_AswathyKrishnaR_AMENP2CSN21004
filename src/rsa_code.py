import rsa
import base64

def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(4096)
    with open('publickey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('privatekey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadPublicKey(keyfile):
    with open(keyfile, 'rb') as p:
        publickeydata = p.read()
        publicKey = rsa.PublicKey.load_pkcs1(publickeydata)
    return publicKey

def loadPrivateKey(keyfile):
    with open(keyfile, 'rb') as p:
        privatekeydata = p.read()
        privateKey = rsa.PrivateKey.load_pkcs1(privatekeydata)
    return privateKey

def rsaencrypt(message, publicKey):
    message_bytes = message.encode('utf-8')
    crypto = rsa.encrypt(message_bytes, publicKey)
    return crypto

def rsadecrypt(crypto, privateKey):
    print(type(crypto))
    message_bytes = rsa.decrypt(crypto, privateKey)
    message = message_bytes.decode('utf-8')  # Convert bytes back to a string
    return message

