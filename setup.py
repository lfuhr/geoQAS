"""
To run before first execution
"""
from setuptools import setup, find_packages


# stanford
import urllib, zipfile, os
print('Downloading stanford-postagger...')
urllib.request.urlretrieve("http://nlp.stanford.edu/software/stanford-postagger-2015-04-20.zip", "stanford.zip")
zipfile.ZipFile('stanford.zip').extractall()
os.remove("stanford.zip")
os.rename("stanford-postagger-2015-04-20", "stanford-postagger")
print('Successfully downloaded stanford-postagger...')

requirements = [l.strip() for l in open('requirements.txt').readlines()][1:]

setup(
    name='${python_package}',
    url='${source_url}',
    version='${python_version}',
    author='${author}',
    author_email='${author_email}',
    description='${description}',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
)
