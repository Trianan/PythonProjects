import requests


def summarize_github_repos(language):
    """Summarizes the top Github project repositories."""

    # Make an API call and store the response:
    url = f"https://api.github.com/search/repositories?q=language:{language.lower()}&sort=stars"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")

    # Store the API response in a variable:
    response_dict = r.json()
    print(f"Total repositories: {response_dict['total_count']}")

    # Explore info about repositories:
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")

    # Examine each repository:
    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        print(f"\tName: {repo_dict['name']}")
        print(f"\tOwner: {repo_dict['owner']['login']}")
        print(f"\tStars: {repo_dict['stargazers_count']}")
        print(f"\tRepository: {repo_dict['html_url']}")
        print(f"\tCreated: {repo_dict['created_at']}")
        print(f"\tUpdated: {repo_dict['updated_at']}")
        print(f"\tDescription: {repo_dict['description']}\n")

    status_code = int(r.status_code)
    return status_code


summary = summarize_github_repos('python')
print(f'\n{summary}')
