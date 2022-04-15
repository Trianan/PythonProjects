your_wallet = 350.00
your_inventory = ''
print(f'You have ${your_wallet}')

in_jimstore = True

print("Jimothy: Welcome to my store!")
print('Jimothy: Here are my prices...')
print('''
        Prices:
    Cigarettes: Regular = $9.25
                Premium = $13.00
    Soda: $2.15
    Chips: $3.50
    Lottery Ticket: Crossword = $5.00
                    Slots = $2.00
                    Jackpot! = $11.11
    Aluminum Foil: $2.45
    Bong: $42                 
''')
number = 0
while in_jimstore == True:

    number += 1
    print(number)
    if number > 1:
        els = ' else'
    else:
        els = ''

    buy = input(f'Would you like to buy anything{els}? y/n: ').lower()
    if buy == 'y':

        item = input('Jimothy: What would you like to buy?: ').lower()
        count = float(input('How many?: '))
        group = ''
        suffix = ''
        if count > 1:
            suffix = 's'
        type = ''
        price = 0

        if item == 'cigarettes':
            group = 'packs '
            cig_type = input('Jimothy: Regular or premium?: ')

            if cig_type.lower() == 'regular':
                type = "'Next Blue' "
                price = 9.25

            elif cig_type.lower() == 'premium':
                type = "'Belmont' "
                price = 13.00

            else:
                print('What?')

        elif item == 'soda':
            group = 'bottles of '
            price = 2.15

        elif item == 'chips':
            group = ' bags of'
            price = 3.50

        elif item == 'aluminum foil':
            group = 'rolls of '
            price = 2.45

        elif item == 'lottery ticket':
            ticket_type = input('''"Crossword", "Slots", or "Jackpot?"''').lower()
            if ticket_type == 'crossword':
                price = 5.00
                type = "'Crossword' "
            elif ticket_type == 'slots':
                price = 2.00
                type = "'Slots' "
            elif ticket_type == 'jackpot':
                price = 11.11
                type = "'Jackpot!' "
            else:
                print('What?')

        elif item == 'bong':
            group = ''
            price = 42.00

        else:
            print('What?')

        your_wallet -= (price * count)
        your_inventory += (f'{type}{item}, ' * int(count))
        print(f'You bought {int(count)} {group}{type}{item}{suffix}.')
        print(f'You have ${your_wallet} left.')
        print(your_inventory)

    elif buy == 'n':
        print('Jimothy: Then get out!')
        print('You leave the store.')
        if 'bong' in your_inventory:
            print('You drop the glass bong on the ground. It smashes on the hard pavement.')
        if 'lottery ticket' in your_inventory:
            print('You scratch your lottery ticket with a coin, hoping for a lucky break...')
            if "'Slots' lottery ticket" in your_inventory:
                print('''You slowly and sequentially scratch away the surface, revealing three beautiful dollar signs. 
You win $10,000,000 and soon retire to a private estate in Cuba at the young age of 30,
living off of investments you made with your winnings.
''')
            else:
                print('You lose.')

        in_jimstore = False

    else:
        print('What?')

