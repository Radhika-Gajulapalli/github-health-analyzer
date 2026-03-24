from github_api import get_repo_data
from health_score import calculate_score

repo = input("Enter repository (owner/repo): ")

stars, forks, issues = get_repo_data(repo)

score = calculate_score(stars, forks, issues)

print("\nRepository Analysis")
print("---------------------")

print("Stars:", stars)
print("Forks:", forks)
print("Open Issues:", issues)

print("\nHealth Score:", score, "/10")