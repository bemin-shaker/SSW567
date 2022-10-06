import requests


def getRepoData(user_id):
    data = requests.get(f'https://api.github.com/users/{user_id}/repos')
    repoList = []

    if data:
        data = data.json()
        for repo in data:
            repoName = repo['name']
            commits = requests.get(
                f'https://api.github.com/repos/{user_id}/{repoName}/commits')
            if commits:
                repoList.append((repoName, len(commits.json())))
            else:
                return f"Error: request to retrieve commits data from repo '{repoName}' returned an error with status code {commits.status_code}"
        return repoList
    else:
        return f"Error: request to retrieve repo data returned an error with status code {data.status_code}"


def main():
    user = input("Enter a user's Github ID: ")
    result = getRepoData(user)
    if not isinstance(result, list):
        print(result)
    for repo in result:
        print(repo[0] + ":", repo[1])


if __name__ == '__main__':
    main()
