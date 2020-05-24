# TwitCommit
Post latest repo commit message to Twitter

## Setup
1. Head on over to https://developer.twitter.com/en/apps and "Create an app"

2. Once your app is created, you'll generate some keys and tokens. Those keys and tokens, you'll provide within the ```config``` file, which is part of this repo. The ```config``` file, should look something like this when you're done with it:

```
[main]
api_key=09123987oje0912jloadj09asfdlb
api_secret_key=lkasjd0912sjad019qwud
access_token=012lksand012lsknd98ausd
access_token_secret=1029laksdnlsand0912ulsand
message=message.txt
```

3. Install the requirements. (python-twitter, beautifulsoup)

```
pip install -r requirements.txt
```

## Usage

TwitCommit.py takes a URL to a GitHub repo as an argument to the ```-repourl``` parameter:

```
$ python TwitCommit.py -repourl https://www.github.com/user/repo
```

The above will parse the latest commit message for the repo, save it to ```message.txt```, and post it to the twitter account via the API details configured within the ```config``` file.

