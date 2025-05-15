import os
import git

def clone_repo(repo_url, clone_dir="cloned_repo"):
    if os.path.exists(clone_dir):
        print(f"Using existing repo at {clone_dir}")
        return clone_dir
    git.Repo.clone_from(repo_url, clone_dir)
    return clone_dir
