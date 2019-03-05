# Author: Jennifer Cafiero
# I pledge my honor that I have abided by the Stevens Honor System.

import requests
import json

def list_github_user_repos(ID):
    ''' You should write a function that will take as input a GitHub user ID.
        The output from the function will be a list of the names of the
        repositories that the user has, along with the number of commits
        that are in each of the listed repositories. '''
    user_repos = []
    repos_url = "https://api.github.com/users/" + ID + "/repos"
    repo_request = requests.get(repos_url)
    repos = repo_request.json()
    for repo in repos:
        commits_url = "https://api.github.com/repos/" + ID + "/"+ repo["name"] + "/commits"
        commits_request = requests.get(commits_url)
        commits = commits_request.json()
        print("Repo: " + repo["name"] + " Number of commits: " + str(len(commits)))
        user_repos.append((str(repo["name"]), len(commits)))

    return user_repos

if __name__ == "__main__":
    list_github_user_repos("jcafiero")
