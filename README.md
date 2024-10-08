﻿# -vigenere_autokey_decrypt
Vigenere Autokey Cipher Decryption using Brute Force
This Python script is designed to decrypt a ciphertext that has been encoded using the Vigenere cipher in Autokey mode. In this mode, the key consists of a short "primer" followed by the plaintext itself. The goal of this script is to recover the plaintext and the primer through a brute-force approach using a dictionary of common English words.

How It Works
Vigenere Autokey Decryption:

The script includes a function vigenere_autokey_decrypt that takes the ciphertext and a primer as inputs.
It uses the primer to decrypt the ciphertext by generating the key using the primer and the decrypted plaintext as it progresses.
The function preserves spaces and punctuation in the ciphertext during decryption.
Brute Force Decryption:

The brute_force_decrypt function attempts to decrypt the ciphertext by trying every word in a provided dictionary file (common_english_words.txt) as the primer.
For each word, it uses vigenere_autokey_decrypt to generate a potential plaintext.
It then checks if the resulting plaintext is valid English using a simple heuristic in is_plausible_english.
Checking for Plausible English:

The is_plausible_english function checks if the decrypted text contains common English words.
It counts the occurrences of some of the most common English words, and if more than 20% of the words in the text are common, it considers the text as plausible English.
Requirements
A text file named common_english_words.txt containing a list of common English words (one word per line). This file is used to guess potential primers.
Python 3.x to run the script.
Usage
Place the common_english_words.txt file in the same directory as the script. This file should contain common English words.
Run the script. It will attempt to decrypt the ciphertext using each word in the dictionary as a potential primer.
The script will print the decrypted plaintext and the primer if successful.
