# galley-sdk

This is a Python SDK for interacting with the graphql API published by Galley (references: [Galley Homepage](https://www.galleysolutions.com/); [Galley API Explorer](https://api.galleysolutions.com/voyager)). Currently maintained by the engineering team at [Thistle](www.thistle.co) but open to PRs from others.


## Installation
For development install with `python setup.py install`

To install within your application
```angular2html
import galley

galley.api_key = <YOUR_API_KEY>
galley.api_url = <YOUR_API_URL>
```