# Input-value index check-er-tron 3000 Version 0.1:

while True:
    input_letter = input('Enter letter: ')

    # This checks if the input is one of the acceptable string-values as defined in "list" ->
    # -> and continues to run the rest of the program if so:
    list = ['a', 'b', 'c', 'd']
    if input_letter in list:
        index_of_input = list.index(input_letter)
        print(index_of_input)

        # This checks if the index of the letter is equal to one of the numbers in "list_numbers":
        list_numbers = [0, 1]
        if index_of_input in list_numbers:
            print("True")
            if index_of_input == 0:
                print("index of input = 0")
            elif index_of_input == 1:
                print("index of input = 1")
        else:
            print("False")
        break

    # This loops back around to the input if the letter is not one of the acceptable ones as defined in "list"
    if input not in list:
        print("Invalid input! ")
