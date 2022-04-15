from counter_function import count_specific_word

print('\nWORD COUNTER-TRONIC: Version 0.1 (TriSon Inc.)')
active = True

while active:
    filename = input('\nWhat file would you like to search from?: ')

    # This section filters and counts the number of words in the specified text file:
    while True:
        word = input("\nSearch for a word in this file (or type 'q' to quit): ").rstrip()
        if word == 'q':
            break

        # word_list = word_raw.split()
        # for word in word_list:

        count_specific_word(filename, word)

    # This section is a simple exit-interaction that modifies the flag set at the beginning of the main loop:
    while True:
        new_file = input('\nWould you like to choose another file to search through? (y/n): ')
        if new_file == 'y':
            active = True
            break
        elif new_file == 'n':
            active = False
            print('\nTerminating program...')
            break
        else:
            print('Invalid input!')