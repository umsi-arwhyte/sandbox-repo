# Project setup

Open the terminal.

## 1.0 git config (minimal setup)

```commandline
git config --list
```

If your name and email address are not set add them to local `.gitconfig` file.

```commandline
git config --global user.name "First and Last name"
git config --global user.email "email address associated with github account"
```

## 2.0 Secure shell (SSH) public / private key

```commandline
ls -al ~/.ssh
```

If no private/public keys exist (e.g., `id_rsa`, `id_rsa.pub`), generate a new 4096 bit RSA key.

```commandline
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

1. When prompted "Enter a file in which to save the key," press Enter and accept the default location.
2. When prompted for a passphrase per the following [ssh.com recommendations](https://www.ssh.com/ssh/passphrase):

    > A good passphrase should have at least 15, preferably 20 characters and be difficult to guess.
    > It should contain upper case letters, lower case letters, digits, and preferably at least one
    > punctuation character. No part of it should be derivable from personal information about the
    > user or his/her family.

### 2.1 Add key to ssh-agent (macOS users)

Start the ssh-agent.

```commandline
eval "$(ssh-agent -s)"
```

Check if a SSH `config` file exists.

```commandline
open ~/.ssh/config
```

If file does not exist create it.

```commandline
touch ~/.ssh/config
```

Open `config` file and add the following lines:

```commandline
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa
```

Add your SSH key. Note that the `-K` flag stores your RSA key's passphrase in your keychain.

```commandline
ssh-add -K ~/.ssh/id_rsa
```

### Register SSH public key with Github

Copy your newly minted public key to the clipboard.

```commandline
pbcopy < ~/.ssh/id_rsa.pub
```

or print your public key to the screen, highlight it, and then copy it to the clipboard
(macOS: `CMD + C`).

```commandline
cat ~/.ssh/id_rsa.pub
```

Visit your Github site.

1. In the upper-right corner of any page, click your profile icon, then click
Settings.
2. In the user settings sidebar, click SSH and GPG keys.
3. Click New SSH key or Add SSH key.
4. In title field provide a title (I use the email address at the end of the public key).
5. Paste your public key in the key field.
6. Click Add SSH key (you will be prompted to re-authenticate).

### Refresh your terminal session

Either quit your terminal session and restart a new session or refresh the existing session with the
`source` command referencing the relevant profile.

```commandline
source ~/.bash_profile
or
source ~/.zsh_profile
or
source ~/.zshrc
```

## 3.0 Fork and clone Github repo (exercise)

### 3.1 Create new repo

* Add .gitignore
* Add LICENSE
* Add README

### 3.2 Fork and clone repo

__Fork__: create a __remote__ copy of a repo that is linked to your Github profile. In a collaborative
team environment each developer maintains their own fork and remotes. Changes to the "upstream" repo
are proposed via the Github pull request workflow. In such a scenario forks must be regularly sync'd
to the repo from which they where forked in order to avoid going stale.

Visit the Github organization or account that contains the repo that you wish to fork. Click the
"Fork" button (upper right) and select the account to which the fork will be added.

__Clone__: create a __local__ copy of a repo on your computer and sync between one or more locations.

Once the repo has been forked, click the green "Code" button, copy the repo link and clone the repo
to an appropriate directory on your local machine.

```commandline
git clone git@github.com:your_account_name/practice_repo.git
```

### 3.3 Update remotes

At a minimum you need to add a new remote that points at the upstream repo that you forked. You will
use the second remote to keep our local clone and our own remote fork in sync with upstream changes.

Check remotes.

```commandline
git remote -v

origin git@github.com:your_account_name/practice_repo.git (fetch)
origin git@github.com:your_account_name/practice_repo.git (push)
```

Change "origin" alias to your Github account name (optional).

```commandline
git remote rename origin your_account_name
```

Add remote.

```commandline
git remote add arwhyte git@github.com:arwhyte/practice_repo.git
```

Confirm remotes.

```commandline
git remote -v

some_account_name git@github.com:some_account_name/practice_repo.git (fetch)
some_account_name git@github.com:some_account_name/practice_repo.git (push)
arwhyte git@github.com:arwhyte/practice_repo.git (fetch)
arwhyte git@github.com:arwhyte/practice_repo.git (push)
```

### Edit README

Edit readme then stage, commit, push and issue a pull request against the upstream repo.

Command sequence

```commandline
git status
git add README.md
git status
git commit -m "..."
git push some_account_name master

git pull arwhyte master
pit push push some_account_name master
```

## Virtual environments

__macOS__

```commandline
python3 -m pip list
python3 -m pip install virtualenv venv
```

Create a virtual environment.

```commandline
cd path_to_practice_project
virtualenv venv
source venv/bin/activate
python3 -m pip list
python3 -m pip install requests
python3 -m pip freeze > requirements.txt
```

Fresh install (read from requirements.txt)

```commandline
python3 -m pip install -r requirements.txt
```

__Windows 10__

```commandline
python -m pip list
python -m pip install virtualenv venv
```

Create a virtual environment.

```commandline
cd path_to_practice_project
virtualenv venv
source venv/Scripts/activate
python -m pip list
python -m pip install requests
python -m pip freeze > requirements.txt
```

Note: if Windows can't find virtualenv then a `PATH` issue exists. Create a virtual environment
using Python 3.x native `venv`.

```commandline
cd path_to_practice_project
python venv venv
```

Fresh install (read from requirements.txt)

```commandline
python3 -m pip install -r requirements.txt
```
