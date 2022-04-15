def generate_tabula_recta():
    """Generates a tabula-recta that includes integer digits for cryptography purposes."""

    tabula_recta = {}

    # List of all the characters used in the tabula-recta:
    tab_seeder = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', ',', '.', '!']

    # If this is not done the actual tab_seeder is modified.
    permutation = tab_seeder.copy()
    for character in tab_seeder:

        # I have no idea why I need this here for this function to iterate properly, but okay:
        perm = permutation.copy()
        tabula_recta[character] = perm

        # print(permutation)

        # This permutes each row by moving the first character to the end of the row.
        permuted_character = permutation[0]
        permutation.remove(permutation[0])
        permutation.append(permuted_character)

    return tabula_recta


generate_tabula_recta()

if __name__ == '__main__':
    # Prints formatted version of tabula-recta:
    tabula_recta = generate_tabula_recta()
    for keyword_character, kc_permutation in tabula_recta.items():
        print(f"{keyword_character}: {kc_permutation}")
