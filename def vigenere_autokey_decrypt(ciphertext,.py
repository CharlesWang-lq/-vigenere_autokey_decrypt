def vigenere_autokey_decrypt(ciphertext, primer):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = ''
    key = primer
    index = 0

    print("the inde"+alphabet.index(1))

    for char in ciphertext:
        if char.lower() in alphabet:
            shift = alphabet.index(key[index].lower())
            decrypted_char = alphabet[(alphabet.index(char.lower()) - shift) % 26]
            decrypted_text += decrypted_char
            key += decrypted_char  # Extend the key with the decrypted character
            index += 1
        else:
            decrypted_text += char  # Non-alphabet characters are added as is
    
    return decrypted_text

ciphertext = "Bimx or lvds'x qinpmwea llv twogpt avd omz ucw zhnzbqi hze bpvga vssq axyi rk wlgvskm yjif ldlc ttci sv. -Tcsgpl Lrusgr."
# Testing multiple primers
common_primers = ["example", "cipher", "decode", "attack","pizza"]  # Add more potential primers
for primer in common_primers:
    plaintext = vigenere_autokey_decrypt(ciphertext, primer)
    print(f"Primer: {primer} -> Decrypted text: {plaintext[:100]}...")
