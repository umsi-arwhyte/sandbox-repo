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
git clone git@github.com:your_account_name/sandbox-repo.git
```

### 3.3 Update remotes

At a minimum you need to add a new remote that points at the upstream repo that you forked. You will
use the second remote to keep our local clone and our own remote fork in sync with upstream changes.

Check remotes.

```commandline
git remote -v

origin git@github.com:your_account_name/sandbox-repo.git (fetch)
origin git@github.com:your_account_name/sandbox-repo.git (push)
```

Change "origin" alias to your Github account name (optional).

```commandline
git remote rename origin your_account_name
```

Add remote using your Github account name.

```commandline
git remote add arwhyte git@github.com:arwhyte/sandbox-repo.git
```

Add a second remote that adds the upstream umsi-arwhyte sandbox-repo.

```commandline
git remote add umsi-arwhyte git@github.com:umsi-arwhyte/sandbox-repo.git
```

Confirm remotes.

```commandline
git remote -v

arwhyte git@github.com:arwhyte/sandbox-repo.git (fetch)
arwhyte git@github.com:arwhyte/sandbox-repo.git (push)
umsi-arwhyte git@github.com:umsi-arwhyte/sandbox-repo.git (fetch)
umsi-arwhyte git@github.com:umsi-arwhyte/sandbox-repo.git (push)
```

## Virtual environment

I use the [virtualenv](https://pypi.org/project/virtualenv/) package to create my Python virtual environments. Python 3.x also provide a `venv` module that you can use.

:exclamation: if Windows can't find virtualenv then a `PATH` issue may exist. Create a virtual
environment using Python 3.x native `venv`.

Below are the commands required to create a virtual environment that is provisioned with its own
Python binary (same version as that used to create the virtual environment).

#### macOS: virtualenv

```commandline
python3 -m pip install virtualenv
cd path/to/project
virtualenv venv
source venv/bin/activate
```

#### Windows 10: venv (Git Bash)

```commandline
cd path/to/project
python -m venv venv
venv/Scripts/activate
```

#### Windows 10: venv (cmd.exe)

```commandline
cd path/to/project
python -m venv venv
C:\venv\Scripts\activate
```

Once the virtual environment is created and activated, additional Python packages can be installed
and managed using a `requirements.txt` file.

:bulb: once activated the command prompt will be prefixed with the name of your virtual environment
between parentheses.

```commandline
(venv) . . .
```

Install the requests package using `pip`. Once installed review the installed packages.

#### macOS

```commandline
python3 -m pip install requests
python3 -m pip list
```

#### Windows 10

```commandline
python -m pip install requests
python -m pip list
```

```commandline
Package    Version
---------- ---------
certifi    2020.12.5
chardet    3.0.4
idna       2.10
pip        20.3.1
requests   2.25.0
setuptools 51.0.0
urllib3    1.26.2
wheel      0.36.1
```

### Requirements files

Requirements files provide a list of required project packages. You can _freeze_ the current set of dependencies and writing package and version information to a `requirements.txt` file.


#### macOS

```commandline
python3 -m pip freeze > requirements.txt
```

#### Windows 10

```commandline
python -m pip freeze > requirements.txt
```

Team members and others who fork/clone your project can install all required project dependencies
by having `pip` read `requirements.txt`.

#### macOS

```commandline
python3 -m pip install -r requirements.txt
```

#### Windows 10

```commandline
python -m pip install -r requirements.txt
```

### Git exercise

Create a Python file named `< uniqname >.py`. Use the `requests` module to issue an HTTP GET
request and retrieve a JSON representation of Darth Vader decoded as a `dict` from the Star Wars API (SWAPI).

```python
import requests


endpoint = 'https://swapi.py4e.com/api'
response = requests.get(f"{endpoint}/people/", {'search': 'darth'}).json()
darth_vader = response['results'][0]

print(f"\nDarth Vader = {darth_vader}")
```

#### Command sequence

```commandline
git status
git add < uniqname >.py
git status
git commit -m "..."
git push some_account_name main

git pull < some_account > main
pit push push < some_account > main
```
