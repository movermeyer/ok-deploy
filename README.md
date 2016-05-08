# OK Deploy

A continuous deployment pipeline implementation to transport applications to a runtime context using build-packs.

![logo](https://raw.githubusercontent.com/Feed-The-Web/ok-deploy/master/docs/_static/img/ok-logo-64.png)
 [![Groups](https://img.shields.io/badge/Google_groups-ftw--users-orange.svg)](https://groups.google.com/forum/#!forum/ftw-users)
 [![Travis CI](https://api.travis-ci.org/Feed-The-Web/ok-deploy.svg)](https://travis-ci.org/Feed-The-Web/ok-deploy)
 [![Coveralls](https://img.shields.io/coveralls/Feed-The-Web/ok-deploy.svg)](https://coveralls.io/r/Feed-The-Web/ok-deploy)
 [![GitHub Issues](https://img.shields.io/github/issues/Feed-The-Web/ok-deploy.svg)](https://github.com/Feed-The-Web/ok-deploy/issues)
 [![License](https://img.shields.io/pypi/l/ok-deploy.svg)](https://github.com/Feed-The-Web/ok-deploy/blob/master/LICENSE)
 [![Development Status](https://pypip.in/status/ok-deploy/badge.svg)](https://pypi.python.org/pypi/ok-deploy/)
 [![Latest Version](https://img.shields.io/pypi/v/ok-deploy.svg)](https://pypi.python.org/pypi/ok-deploy/)
 [![Download format](https://pypip.in/format/ok-deploy/badge.svg)](https://pypi.python.org/pypi/ok-deploy/)
 [![Downloads](https://img.shields.io/pypi/dw/ok-deploy.svg)](https://pypi.python.org/pypi/ok-deploy/)


## Overview

“OK Deploy” helps you to deliver applications to their
intended target runtime, and manage them during their life-cycle
while remaining in the data center.
The initial focus is Java web applications and Tomcat 7/8.

The main command line tool is `ok`, which for one is easy to type,
and frankly also allows me to have a `ok computer` sub-command. :smiley:

It is designed to have similarities to `git`'s interface.
“OK” projects are normal `git` repositories, with some conventions on
the file system structure and branch names applied.


## Installation

*OK Deploy* can be installed via ``pip install ok-deploy`` as usual,
see [releases](https://github.com/Build-The-Web/ok-deploy/releases) for an overview of available versions.
To get a bleeding-edge version from source, use these commands:

```sh
repo="Build-The-Web/ok-deploy"
pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"
```

See [Contributing](#contributing) on how to create a full development environment.

To add bash completion, read the [Click docs](http://click.pocoo.org/4/bashcomplete/#activation) about it,
or just follow these instructions:

```sh
cmdname=ok-deploy
mkdir -p ~/.bash_completion.d
( export _$(tr a-z- A-Z_ <<<"$cmdname")_COMPLETE=source ; \
  $cmdname >~/.bash_completion.d/$cmdname.sh )
grep /.bash_completion.d/$cmdname.sh ~/.bash_completion >/dev/null \
    || echo >>~/.bash_completion ". ~/.bash_completion.d/$cmdname.sh"
. "/etc/bash_completion"
```


## Usage

### `ok init`

Create a brand new project in a local working directory.
This is just a wrapper around `git init`, and creates
additional files to form a fully compliant “OK” project.

For version management of changes after that, use `git` as usual.


### `ok clone`

Create a local working directory for a project by getting it from a remote repository.
This is just a wrapper around `git clone`, and allows you
to specify the source by just providing a project name,
that is then found based on OK's configuration.


### `ok computer`

_Makes the computer talk to you._ :grin:

Query information about the project in the current directory,
and other pertinent information about the local and remote environments.


### `ok config`

Manages your local copy of the deployment configuration.


### `ok deploy`

Perform a deployment.


### `ok control`

Control the state of a deployed application.


## Contributing

To create a working directory for this project, call these commands:

```sh
git clone "https://github.com/Feed-The-Web/ok-deploy.git"
cd "ok-deploy"
. .env --yes --develop
invoke build --docs test check
```

See [CONTRIBUTING](https://github.com/Feed-The-Web/ok-deploy/blob/master/CONTRIBUTING.md) for more.


## References

**Tools**

* [Cookiecutter](http://cookiecutter.readthedocs.io/en/latest/)
* [PyInvoke](http://www.pyinvoke.org/)
* [pytest](http://pytest.org/latest/contents.html)
* [tox](https://tox.readthedocs.io/en/latest/)
* [Pylint](http://docs.pylint.org/)
* [twine](https://github.com/pypa/twine#twine)
* [bpython](http://docs.bpython-interpreter.org/)
* [yolk3k](https://github.com/myint/yolk#yolk)

**Packages**

* [Rituals](https://jhermann.github.io/rituals)
* [Click](http://click.pocoo.org/)


## Acknowledgements

[![1&1](https://raw.githubusercontent.com/1and1/1and1.github.io/master/images/1and1-logo-42.png)](https://github.com/1and1)  Project sponsored by [1&1](https://github.com/1and1).
