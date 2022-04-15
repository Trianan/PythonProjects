from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

import requests


# Make an API call and store the response:
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission:
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article:
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        print(f"Missing data for {submission_id}!")
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

comments_total, article_labels = [], []
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

    # Visualization data:
    comments_total.append(int(submission_dict['comments']))
    article_labels.append(f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>")

# Visualization:

data = [{
    'type': 'bar',
    'x': article_labels,
    'y': comments_total,
}]

my_layout = {
    'title': 'Most Discussed Hacker-News Articles',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Article',
        'titlefont': {'size': 24},
        'tickfont': {'size': 7},
    },
    'yaxis': {
        'title': 'Number of comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='saved_figures/hn_submissions.html')
