from setuptools import setup

# Note: The only packages that should be added to the install_requires
# are dependencies that are required on remote installs, not local development.
setup(
    name='galley_sdk',
    version='0.46.0',
    packages=['galley', 'galley.client'],
    install_requires=['sgqlc==14.0', 'backoff==1.11.1', 'httpx>=0.27.0', 'pydantic>=2.0.0']
)
