import git


def collect(url, name):
    try:
        repository = git.Repo(name)
        print('Mise à jour du dépôt...', end='\t')
        repository.remotes.origin.pull()
    except (git.InvalidGitRepositoryError, git.NoSuchPathError):
        print('Création du dépot...', end='\t')
        git.Git('.').clone(url, name)
    print('OK')
