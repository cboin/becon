from setuptools import setup, find_packages


setup(
    name='becon',
    version='1.0',
    description='Password Manager',
    packages=find_packages(),
    scripts=['src/becon.py'],
)
