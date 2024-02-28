from setuptools import setup, find_packages

# Note: The only packages that should be added to the install_requires
# are dependencies that are required on remote installs, not local development.
setup(
    name='galley_sdk',
    version='0.46.0',
    packages=find_packages('galley/'),
    install_requires=['sgqlc==14.0', 'backoff==1.11.1']
)
