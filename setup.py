from setuptools import setup


setup(
    name='galley_api',
    version='0.1.0',
    packages=['galley'],
    install_requires=['sgqlc==14.0', 'mypy==0.770']
)