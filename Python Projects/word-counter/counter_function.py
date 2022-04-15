def count_specific_word(filename, word):
    """Counts the number of times a specific word appears in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"The file {filename} either does not exist, or cannot be found.")
    else:
        # This converts all words to lowercase:
        contents_lowered = contents.lower()

        # This filters all the punctuation and non-letter characters out (except ' so conjugated words are countable):
        character_delete = '''!@#$%^&*()-_+`~<>?/=.,:;"|{}[]'''
        for character in character_delete:
            contents_lowered = contents_lowered.replace(character, '')

        # This adds each individual word to a list, then counts up how many times each word appears:
        # all_words = contents_lowered.split()
        # word_count = all_words.count(word)
        all_words = contents_lowered
        word_count = all_words.count(word)
        # This is necessary as ' is omitted from the character filter, so "'words'" and "words" are counted as the same:
        word_count += all_words.count("'" + word + "'")

        print(f"The file {filename} has {word_count} instances of the word '{word}'.")