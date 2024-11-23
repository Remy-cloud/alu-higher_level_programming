#!/usr/bin/python3
""" script that takes 2 arguments in order to solve this challenge"""
import requests
import sys

if __name__ == "__main__":
    # Get the repository name and owner name from arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    
    # GitHub API URL for commits
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    
    # Send GET request to GitHub API to get commits
    response = requests.get(url)
    
    # If the request was successful, proceed to process the response
    if response.status_code == 200:
        commits = response.json()  # Parse the JSON response
        
        # Loop through the first 10 commits and print the SHA and author name
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: {response.status_code}")

