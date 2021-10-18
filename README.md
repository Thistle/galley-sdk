# galley-sdk

This is a Python SDK for interacting with the graphql API published by Galley (references: [Galley Homepage](https://www.galleysolutions.com/); [Galley API Explorer](https://api.galleysolutions.com/voyager)). Currently maintained by the engineering team at [Thistle](www.thistle.co) but open to PRs from others.


## Installation
To set up your environment and install the required dependencies for local development, you will need both Python and a virtual environment tool like [virtualenv](https://virtualenv.pypa.io/en/latest/#) or [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) installed. These instructions assume you are using virtualenv:
```
$ git clone git@github.com:Thistle/galley-sdk.git
$ cd galley-sdk
$ virtualenv venv
$ . venv/bin/activate
$ python setup.py install
```

To use galley-sdk within your application, you can install from this repository using [pip's version control system support](https://pip.pypa.io/en/stable/topics/vcs-support/#vcs-support).  This example assumes you are using Git:
```
pip install git+git://github.com/Thistle/galley-sdk.git@0.1.0#egg=galley-sdk
```


## Using galley-sdk
After installing, you will need to set up credentials:
```
import galley

galley.api_key = <YOUR_API_KEY>
galley.api_url = <YOUR_API_URL>
```

Then you can use the package to access Galley's API, for example to retrieve recipe data:
```
from galley.queries import get_recipe_data

get_recipe_data()
```

## Tests
To run all unit tests:
`python -m unittest tests/test_*`

To run a specific test:
`python -m unittest tests.test_queries.TestQueryGalleyRecipes.test_get_recipe_data_successful`
