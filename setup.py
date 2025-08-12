from setuptools import setup

# Note: The only packages that should be added to the install_requires
# are dependencies that are required on remote installs, not local development.
setup(
    name='galley_sdk',
    version='1.8.0',
    packages=['galley'],
    install_requires=['sgqlc==14.0', 'backoff>=2.0.0']
)
