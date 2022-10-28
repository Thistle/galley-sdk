# galley-sdk

This is a Python SDK for interacting with the graphql API published by Galley (references: [Galley Homepage](https://www.galleysolutions.com/); [Galley API Explorer](https://api.galleysolutions.com/voyager)). Currently maintained by the engineering team at [Thistle](www.thistle.co) but open to PRs from others.


## Installation
To set up your environment and install the required dependencies for local development, you will may use both Python and a virtual environment tool like [virtualenv](https://virtualenv.pypa.io/en/latest/#) or [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) or the supplied [Development Container](https://containers.dev/).

> :warning: Python version >3.8 is currently unsupported. You will have to downgrade Python (not recommended) or use pyenv-virtualenv to use galley-sdk.

### virtualenv steps
```
$ git clone git@github.com:Thistle/galley-sdk.git
$ cd galley-sdk
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

### pyenv-virtualenv steps
You can install pyenv and pyenv-virtualenv with [brew](https://brew.sh/):
```
brew install pyenv pyenv-virtualenv
```
To use galley-sdk in pyenv-virtualenv:
```
$ git clone git@github.com:Thistle/galley-sdk.git
$ cd galley-sdk
$ pyenv install 3.8.13
$ pyenv virtualenv 3.8.13 py38
$ pyenv activate py38
$ pip install -r requirements.txt
```

> Note: When using galley-sdk in the future, make sure you run `pyenv activate py38` beforehand to be in the correct virtual envrionment.

### Using the supplied Development Container
To use the development container you will need a docker environment installed.  

If you are using VS Code you can then just open the project and you will be prompted to open the project in a container.  

You will not need to install any local python or virtual environments if you use the development container.


### Using galley-sdk in your application:

To use galley-sdk within your application, you can install from this repository using [pip's version control system support](https://pip.pypa.io/en/stable/topics/vcs-support/#vcs-support) to specify a git ref such as a branch name, commit hash, or tag name. This example assumes you are using Git:

```
pip install git+git://github.com/Thistle/galley-sdk.git@<git-ref>#egg=galley-sdk
```

## Configuration
First, you will need to set up credentials. Create a file called `.env` in the root directory of the project and set these two environment variables with your valid credentials for Galley's API:
```
GALLEY_API_KEY=<your-organization's-API-key>
GALLEY_URL=<Galley's-staging-or-production-url>
```

## Using galley-sdk
Now you can use the package to make requests to Galley. For example, to retrieve recipe data:
```
import galley
from galley.queries import get_recipe_data

get_recipe_data()
```

## Tests
To run all unit tests:
`python -m unittest tests/test_*`

To run a specific test:
`python -m unittest tests.test_queries.TestQueryGalleyRecipes.test_get_recipe_data_successful`
