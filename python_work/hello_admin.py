current_usernames = ['jimmy222', 'admin', 'xXxBVBxXx', 'knobkicker69']

current_usernames_lowercase = []
for name in current_usernames:
    current_usernames_lowercase.append(name.lower())
print(current_usernames_lowercase)


new_usernames = ['jimdog44', 'xXxBvbxXX', 'sambamthankumam', 'josh']

for name in new_usernames:
    if name.lower() in current_usernames_lowercase:
        print(f'Username taken: {name}.')
    else:
        print(f'Username available: {name}')