# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:46:51 2020

@author: RDxR10

The cipher used here was the "Hill Cipher". A 3x3 matrix has been utilised.



"""

import numpy as np
from egcd import egcd
encrypted_message = "lkeitrx66dcw{3zy1}tvzlrb4ilp9}1m0ifqjvuu3 1m0h9b5dc ucu3eicw{n}nauu3 95o00jd 0q55x66nwm"
K = np.matrix([[6, 24, 1], [13,16,10], [20,17,15]])



alphanum = "abcdefghijklmnopqrstuvwxyz0123456789{}_ "


letter_to_index = dict(zip(alphanum, range(len(alphanum))))
index_to_letter = dict(zip(range(len(alphanum)), alphanum))

def matrix_mod_inv(matrix, modulus):
   
    det = int(np.round(np.linalg.det(matrix)))  # Step 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3)

    return matrix_modulus_inv

Kinv = matrix_mod_inv(K, len(alphanum))
#print(len(alphanum))

def decrypt(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphanum)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted

def main():
    decrypted_message = decrypt(encrypted_message, Kinv)
    print("Decrypted message: " + decrypted_message)
main()
