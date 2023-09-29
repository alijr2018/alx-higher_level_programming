#!/usr/bin/python3
"""a Python script that takes 2 arguments in order to solve this challenge."""

import requests
import sys

if __name__ == "__main__":
    rep_name = sys.argv[1]
    own_name = sys.argv[2]

    url = "https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    res = requests.get(url)
    commits = res.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
