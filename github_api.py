import requests

def get_repo_data(repo):

    url = f"https://api.github.com/repos/{repo}"

    response = requests.get(url)

    data = response.json()

    stars = data["stargazers_count"]
    forks = data["forks_count"]
    issues = data["open_issues_count"]

    return stars, forks, issues