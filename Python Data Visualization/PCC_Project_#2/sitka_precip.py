import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/buffalo-2013-2021-precip.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Get high temperatures from this file:
    dates, precip_data = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            precipitation = float(row[header_row.index('PRCP')])
        except ValueError:
            print(f'Precipitation data not available for {current_date}!')
        else:
            dates.append(current_date)
            precip_data.append(precipitation)
        station_name = row[header_row.index('NAME')]

# Plot the high temperatures:
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precip_data, c='green')

# Format plot:
title = f'Daily Precipitation - 2013-2021\n{station_name}'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Precipitation', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.savefig(f'saved_figures/precipitation_{station_name}.png')
plt.show()



