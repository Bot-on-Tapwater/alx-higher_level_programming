#!/usr/bin/python3
"""Print last 10 commits of a repo owned by a user"""
import requests
import sys


def get_commits(owner, repo):
    base_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(base_url)

    if response.status_code == 200:
        commits = response.json()[:10]
        return commits
    else:
        sys.exit(1)


def print_commits(commits):
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    commits = get_commits(owner_name, repo_name)
    print_commits(commits)
