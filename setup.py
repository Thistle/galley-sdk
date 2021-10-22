from setuptools import setup


setup(
    name='galley_sdk',
    version='0.3.1',
    packages=['galley'],
    install_requires=['sgqlc==14.0', 'mypy==0.770', 'backoff==1.11.1']
)
