import string

# Function to decrypt the ciphertext using the guessed primer
def vigenere_autokey_decrypt(ciphertext, primer):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = ''
    key = primer
    idx = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = alphabet.index(key[idx % len(key)].lower())  # Ensure key is lowercase
            if char.islower():
                original_index = (alphabet.index(char) - shift) % 26
                decrypted_char = alphabet[original_index]
            else:
                original_index = (alphabet.index(char.lower()) - shift) % 26
                decrypted_char = alphabet[original_index].upper()  # Preserve uppercase
                
            decrypted_text += decrypted_char
            key += decrypted_char.lower()  # Append the lowercase version of the decrypted char to the key
            idx += 1
        else:
            decrypted_text += char  # Preserve non-alphabet characters
            
    return decrypted_text

# Brute force attempt to guess the primer
def brute_force_decrypt(ciphertext):
    # Load a list of common English words (from a text file)
    with open('common_english_words.txt', 'r') as f:
        english_words = [word.strip().lower() for word in f]

    for primer in english_words:
        decrypted_text = vigenere_autokey_decrypt(ciphertext, primer)
        if is_plausible_english(decrypted_text):
            return decrypted_text, primer

    return "No valid plaintext found.", None

# Check if the decrypted text looks like English
def is_plausible_english(text):
    common_words = ['the', 'and', 'to', 'of', 'a', 'in', 'that', 'is', 'it', 'was', 'are', 'not', 'do', 'did', 'were']  # Common English words
    word_count = 0
    words = text.split()
    for word in words:
        if word.lower() in common_words:
            word_count += 1
    # If more than 20% of the words are common English words, it's plausible English
    return word_count > len(words) * 0.2

ciphertext = "Bimx or lvds'x qinpmwea llv twogpt avd omz ucw zhnzbqi hze bpvga vssq axyi rk wlgvskm yjif ldlc ttci sv. -Tcsgpl Lrusgr."
decrypted_text, primer = brute_force_decrypt(ciphertext)

print("Decrypted Text:", decrypted_text)
print("Primer:", primer)
