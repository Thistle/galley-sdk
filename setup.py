from setuptools import setup


setup(
    name='galley_sdk',
    version='0.7.0',
    packages=['galley'],
    install_requires=['sgqlc==14.0', 'backoff==1.11.1']
)
