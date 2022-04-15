import matplotlib.pyplot as plt
from die import Die


die_1 = Die()
die_2 = Die()


results = [die_1.roll() + die_2.roll() for roll_num in range(10_000)]
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

plt.style.use('dark_background')
fig, ax = plt.subplots()

ax.bar(range(2, max_result+1), frequencies, color='red')

ax.set_title('2 D6 Dice Roll Results', fontsize=30)
ax.set_xlabel('Results')
ax.set_ylabel('Frequency of Result')
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_xticks(range(2, max_result+1))

plt.show()