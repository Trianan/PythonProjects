# "Vingenère" Cryptography Tool: Version Beta
# TO DO: add read/write support for file functionality and rework program flow to allow quitting from mode selection.
from vigenere_cipher import VingenereCipher


print("\nWelcome to the 'Vingenère' Cryptography Tool! (Version Beta)\n")
while True:

    # Keyword Entry:
    keyword = input("\nPlease enter your keyword now (or type 'q' to quit): ")
    if keyword == 'q':
        break
    else:
        cipher = VingenereCipher(keyword)

    # Mode Selection:
    while True:
        mode = input("\nWould you like to encrypt (e) or decrypt (d)?: ")

        # Encryption Mode:
        if mode.lower() == 'e':
            plaintext = input("Please enter the plaintext you wish to encrypt ('q' to quit): ")
            if plaintext == 'q':
                print('Quitting...')
                break
            else:
                encrypted_text = cipher.encrypt(plaintext)
                print(encrypted_text)

        # Decryption Mode:
        elif mode.lower() == 'd':
            ciphertext = input("Please enter the ciphertext you wish to decrypt ('q' to quit): ")
            if ciphertext == 'q':
                print('Quitting...')
                break
            else:
                decrypted_text = cipher.decrypt(ciphertext)
                print(decrypted_text)

        else:
            print('That is not a valid mode!')

        new_loop = input('Would you like to choose another keyword/quit? (y/n): ')
        if new_loop.lower() == 'y':
            break
        elif new_loop.lower() == 'n':
            continue
        else:
            'That is not a valid input!'


