import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    latitudes, longitudes, brightnesses = [], [], []
    for row in reader:
        try:
            latitude = float(row[header_row.index('latitude')])
            longitude = float(row[header_row.index('longitude')])
            brightness = float(row[header_row.index('brightness')])
        except ValueError:
            continue
        else:
            latitudes.append(latitude)
            longitudes.append(longitude)
            brightnesses.append(brightness)

data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'marker': {
        'color': brightnesses,
        'colorscale': 'Hot',
        'colorbar': {'title': 'Fire Brightness'}
    },
}]

my_layout = Layout(title='World Wildfires: 2018-09-22')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_wildfires_2018-09-22.html')
