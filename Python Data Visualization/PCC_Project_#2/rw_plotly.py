import plotly.express as px

from random_walk import RandomWalk


random_walk = RandomWalk()
random_walk.fill_walk()
order = list(range(1, len(random_walk.x_values)+1))
fig = px.scatter(x=random_walk.x_values, y=random_walk.y_values, color=order)
fig.show()
