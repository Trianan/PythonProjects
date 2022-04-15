age = 13

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teen'
elif age < 65:
    stage = 'adult'
elif age >= 65:
    stage = 'elder'


if stage == 'adult':
    a = 'an'
else:
    a = 'a'

print(f"You are {a} {stage}.")