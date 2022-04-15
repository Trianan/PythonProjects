from tabula_recta import generate_tabula_recta


class VingenereCipher:
    """A class that represents the encryption and decryption algorithms for the 'Vingenère Cipher'."""

    def __init__(self, keyword):
        """Initializes data used for cipher functions."""
        self.plaintext_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6',
                                     '7', '8', '9', '0', ' ', ',', '.', '!']
        self.keyword = keyword
        self.tabula = generate_tabula_recta()

    def encrypt(self, plaintext):
        """Takes indices returned from "index_plaintext() and a keyword,
        and returns an encrypted version of original plaintext"""

        encrypted_string = ''
        plaintext = plaintext.lower()
        # This next line ensures that the keyword "loops" if it is shorter than the plaintext; it's a hack:
        self.keyword *= len(plaintext)

        for i in range(len(plaintext)):
            # Assigns each character in plaintext to a temporary variable "p_i":
            p_i = plaintext[i]
            # Assigns each character in the keyword to a temporary variable "k_i":
            k_i = self.keyword[i]
            # Selects the permutation associated with each keyword character in the tabula-recta:
            t_i = self.tabula[k_i]
            # Selects each permutation's character that shares the same index value as each plaintext character:
            plainchar_index = self.plaintext_characters.index(p_i)
            encrypted_char = t_i[plainchar_index]
            # Builds the final encrypted product with the encrypted characters:
            encrypted_string += encrypted_char
        return encrypted_string

    def decrypt(self, ciphertext):
        """Takes ciphertext characters, converts them into their associated permutation's indices, then decrypts them into
        their original plaintext form."""
        decrypted_string = ''
        self.keyword *= len(ciphertext)

        for i in range(len(ciphertext)):
            # Assigns each character in ciphertext to temporary variable "c_i":
            c_i = ciphertext[i]
            # Assigns each character in keyword to temporary variable "k_i":
            k_i = self.keyword[i]
            # Selects the permutation associated with each keyword character in the tabula-recta:
            t_i = self.tabula[k_i]
            # Selects each plaintext character that shares the same index value as each ciphertext character:
            permutation_keychar_index = t_i.index(c_i)
            decrypted_character = self.plaintext_characters[permutation_keychar_index]
            # Builds the final decrypted product with the decrypted characters:
            decrypted_string += decrypted_character
        return decrypted_string


# Test calls:

if __name__ == '__main__':
    plain = 'i hate mondays, they suck'
    key = 'popsicle'
    print(f"\nPlaintext: {plain}\nKeyword: {key}\n")

    cipher = VingenereCipher(key)

    print("Beginning encryption with 'Vingenère Cipher'...\n")
    encrypted_plaintext = cipher.encrypt(plain)
    print(encrypted_plaintext)

    print(f"\nBeginning decryption with 'Vingenère Cipher'...\n")
    decrypted_ciphertext = cipher.decrypt(encrypted_plaintext)
    print(decrypted_ciphertext)
