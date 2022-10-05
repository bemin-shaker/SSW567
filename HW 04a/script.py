
import requests
import json


def fetchRepos(user_id):
    repo_api = "https://api.github.com/users/"
    commit_api = "https://api.github.com/repos/"

    list_of_repo = []
    commits = []

    repo_url = repo_api + f'{user_id}/' + 'repos'

    try:
        repo_url = requests.get(url=repo_url)
    except (TypeError, KeyError, IndexError):
        return "Failed to fetch the repos"

    repo_url = json.loads(repo_url.text)

    for repository in repo_url:
        try:
            list_of_repo.append(repository['name'])
        except (TypeError, KeyError, IndexError):
            return "Repository name doesn't exist"

    for r in list_of_repo:
        commit_url = commit_api + f'{user_id}/{r}/commits'

        try:
            res = requests.get(url=commit_url)
        except (TypeError, KeyError, IndexError):
            return "Failed to fetch the commits"

        res_json = json.loads(res.text)
        commits.append(f'Repo: {r}  Number of commits: {len(res_json)}')

    return commits


def main():
    user = input("Enter user's Github ID: ")
    for repo in fetchRepos(user):
        print(repo)


if __name__ == '__main__':
    main()
