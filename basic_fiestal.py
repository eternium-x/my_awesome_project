# BASIC FIESTAL CIPHER

import hashlib
import base64
import binascii

salt = "this is pretty amazing salt"


def xor(s1, s2):
    # s1, s2 are str
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def key_256(key):
    return hashlib.sha256((key + salt).encode()).hexdigest()


def scramble(data, key, i):
    # data, key in str
    # str -> bin -> int

    data = ''.join(['{:08b}'.format(ord(i)) for i in str(data)])
    key = ''.join(['{:08b}'.format(ord(i)) for i in str(key)])

    data = int(data, 2)
    key = int(key, 2)

    result = pow((data * key), i)
    res = bin(result)

    # return ''.join(chr(int(res[i: i+8], 2)) for i in )

    return ''.join([chr(int(bin(result)[i:i + 8], 2)) for i in range(0, len(bin(result)), 8)])


def encrypt(key, message, mode):
    cipher = ''
    rounds = 8
    blocksize = 8

    message = [message[i:i + blocksize] for i in range(0, len(message), blocksize)]
    if len(message[-1]) < blocksize:
        message[-1] += ' ' * (blocksize - len(message[-1]))
    print(message)

    key = key_256(key)
    initial_key = key

    for block in message:
        L = [""] * (rounds + 1)
        R = [""] * (rounds + 1)

        L[0] = block[:blocksize // 2]
        R[0] = block[blocksize // 2:]

        # print('L', L)
        # print('R', R)
        # print()

        for i in range(1, rounds + 1):
            L[i] = R[i - 1]

            if mode == 'cbc':
                if i == 1:
                    key = initial_key
                else:
                    key = hashlib.sha256((L[i] + initial_key).encode()).hexdigest()

            R[i] = xor(L[i - 1], scramble(R[i - 1], key, i))

        cipher += L[rounds] + R[rounds]
    # print('L', L)
    # print('R', R)
    # print()
    print(cipher)
    return cipher


c = encrypt('important', 'this is confidential', 'cbc')
c = bytearray(c.encode())
print(binascii.hexlify(c))
print(base64.b64encode(c))
