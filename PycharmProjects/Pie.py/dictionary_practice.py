usernames = {
    'tommak101': {'full_name': 'thomas makkel', 'age': 34, 'profession': 'fisherman'},

    'ferrousman98': {'full_name': 'frank borger', 'age': 27, 'profession': 'carpenter'},

    'jmth666': {'full_name': 'jimothy jones', 'age': 69, 'profession': 'unemployed'}
    }

for username, user_info in usernames.items():
    print(f"{username}:")
    for key, value in user_info.items():
        full_name = user_info['full_name']
        age = user_info['age']
        job = user_info['profession']
    print(f"\tFull name: {full_name.title()}\n\tAge: {age}\n\tProfession: {job}\n")




